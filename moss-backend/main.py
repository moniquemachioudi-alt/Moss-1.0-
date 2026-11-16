import os
import math

from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()                                   # looks for the .env file
SUPABASE_URL = os.getenv("SUPABASE_URL")        # gets the URL 
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")        # gets the KEY 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)    # unlocking, and giving connection

# create the main web application instance
app = FastAPI()

# allow moos-app to request data w/t getting blocked by the web browser
# to be implemented later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# established endpoints for soil moisture
ADC_DRY = 2640;
ADC_SAT = 982;


# initializing the web API applcation 
# defines the data validation blueprint for env sensors readings 
# prepares the backend to receive incoming data
class Reading(BaseModel):
    device_id: str | None = None
    recorded_at: datetime
    raw_adc: int | None = None
    soil_temp_c: float | None = None
    light_lux: float | None = None
    air_temp_c: float | None = None
    air_rh_pct: float | None = None


# Sanity check to see the server is open 
@app.get("/")
def health():
    return {"status": "ok"}


# Receives the incoming packet 
# checks at least one sensor is sending something
@app.post("/readings")
def receive_reading(reading: Reading):
    # print(reading)
    sensor_values = [
        # reading.device_id,
        # reading.recorded_at,
        reading.raw_adc,
        reading.soil_temp_c, 
        reading.light_lux, 
        reading.air_temp_c, 
        reading.air_rh_pct,
    ]

    # if all(value is None for value in sensor_values):
    #         raise HTTPException(
    #             status_code=400, 
    #             detail="Reading has no sensor values. Send at least one of: "
    #             "raw_adc, voltage_v, soil_moisture, soil_temp, "
    #             "light_lux, air_temp, air_humidity.")

    # clean the ADC values & convert raw_adc to %moisture
    clean_adc = None
    soil_moisture_pct = None
    if reading.raw_adc is not None: 
        if not (200 <= reading.raw_adc <= 4094):
            raise HTTPException(status_code=422, detail="Rejected capacitive sensor outlier")
        clean_adc = reading.raw_adc

        # computer %moisture
        pct = ((ADC_DRY - clean_adc) / (ADC_DRY - ADC_SAT)) * 100.0
        soil_moisture_pct = round(max(0.0, min(100.0, pct)), 2)


    # discard any impossible soil_temp readings 
    clean_soil_temp = (
        None        # if the data is broken, sets clean_soil_temp to "None"
        if (reading.soil_temp_c is None or math.isnan(reading.soil_temp_c) or reading.soil_temp_c <= -55.0 or reading.soil_temp_c == 85.0)
        else round(reading.soil_temp_c, 2)
    )

    # clean up values for Light reading 
    clean_light_lux = (
        None
        if (reading.light_lux is None or math.isnan(reading.light_lux) or reading.light_lux < 0)
        else round(reading.light_lux, 2)
    )

    # clean up values for Air Temp reading   
    clean_air_temp = (
        None
        if (reading.air_temp_c is None or math.isnan(reading.air_temp_c) or not (-40.0 <= reading.air_temp_c <= 85.0))
        else round(reading.air_temp_c, 2)
    )

    # clean up values for Air RH reading
    clean_air_rh = (
        None
        if (reading.air_rh_pct is None or math.isnan(reading.air_rh_pct) or not (0.0 <= reading.air_rh_pct <= 100.0))
        else round(reading.air_rh_pct, 2)
    )

    # make sure the timestaps is valid 
    if reading.recorded_at.year < 2023:
        recorded_iso = datetime.now(timezone.utc).isoformat()
    else: 
        recorded_iso = reading.recorded_at.isoformat()


    # Insert a row into Supabase readings table 
    row = {
        "device_id": reading.device_id,
        "recorded_at": recorded_iso,
        "raw_adc": clean_adc,
        "soil_moisture_pct": soil_moisture_pct,
        "soil_temp_c": clean_soil_temp,
        "light_lux": clean_light_lux, 
        "air_temp_c": clean_air_temp, 
        "air_rh_pct": clean_air_rh,
    }


    try: 
        supabase.table("readings").insert(row).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insert failed: {str(e)}")

    return {"RECEIVED":True, "soil_moisture_pct": soil_moisture_pct}



    # device_id text not null references devices(device_id),
    # recorded_at timestamptz not null default now(),
    # raw_adc real,
    # soil_moisture_pct real, 
    # soil_temp_c real, 
    # light_lux real, 
    # air_temp_c real,
    # air_rh_pct real,
    # plant_id uuid references plants(plant_id),
    # primary key (device_id, recorded_at)