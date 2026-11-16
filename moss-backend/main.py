from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Reading(BaseModel):
    device_id: str 
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
        print(reading)
        sensor_values = [
             reading.recorded_at,
             reading.raw_adc,
             reading.soil_temp_c, 
             reading.light_lux, 
             reading.air_temp_c, 
             reading.air_rh_pct,
        ]

        if all(value is None for value in sensor_values):
             raise HTTPException(
                  status_code=400, 
                  detail="Reading has no sensor values. Send at least one of: "
                   "raw_adc, voltage_v, soil_moisture, soil_temp, "
                   "light_lux, air_temp, air_humidity.")

        return {"RECEIVED":True}