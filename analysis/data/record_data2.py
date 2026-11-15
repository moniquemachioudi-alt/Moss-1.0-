# Version 2: implemenration of SOIL MOISTURE & TEMP
import serial

import time
from datetime import datetime
import math

PORT = "/dev/cu.usbserial-0001"  # Confirm with ls /dev/cu.usb*
BAUD = 115200


# 1. Prompt for file name (and remove the trailing white spaces)
custom_name = input("Enter file name: ").strip()    

if not custom_name:
    filename = "test_run.csv"
elif not custom_name.endswith(".csv"):
    filename = f"{custom_name}.csv"
else:
    filename = custom_name


# 2. Handshake connection 
try:
    ser = serial.Serial(PORT, BAUD, timeout=2)      # establish seria connection (gives 2 sec to connect)
    time.sleep(2)                                   # Wait for serial handshake
    print(f"Connected to ESP32 on {PORT} at {BAUD} baud.")
except Exception as e:
    print(f"Connection error: {e}")
    print("Ensure the PlatformIO Serial Monitor in VS Code is closed!")
    exit(1)


# 3. creating the file
with open(filename, "w", encoding="utf-8") as f:

    # Scientific header to follow SQL HEADER
    header = "recorded_at, ELAPSED_TIME_s, raw_adc, soil_temp_c, light_lux, air_temp_c, air_rh_pct\n"
    f.write(header)
    f.flush()       #forces Python's internal buffer to write the header directly to mac storage disk
    print(f"Logging data to {filename}... Press Ctrl+C to stop.")
    print("-" * 65)

    start_time = None

    try:
        while True:

            # reads the new data bytes and converst to clean Python string 
            raw_line = ser.readline().decode("utf-8", errors="ignore").strip() 

            if not raw_line:
                continue

            # Filter out boot prints or headers (checks anywhere in the line)
            if any(
                word in raw_line
                for word in ["ELAPSED", "recorded", "===", "ESP32", "rst:"]
            ):
                continue



            # Time normalization aka, start at 0s
            parts = raw_line.split(",")

            # Expecting 4 values from firmware: recorded_at, ELAPSED_TIME_s, raw_adc, soil_temp_c, light_lux, air_temp_c, air_rh_pct
            if len(parts) == 7:
                try: 
                    esp_time = int(parts[0].strip())
                    elapsed_ms = int(parts[1])
                    raw_adc = int(parts[2])
                    # voltage = float(parts[3])
                    soilTemp_raw = float(parts[3])
                    lightLux_raw = float(parts[4])
                    airTemp_raw = float(parts[5])
                    airRH_raw = float(parts[6])
                except ValueError:
                        # Skips corrupted serial lines safely without crashing the script
                        continue


                # Smart fallback: If ESP32 has no Wi-Fi sync yet (time < year 2023), use Mac's real time
                if esp_time < 1700000000:
                    binary_time = int(time.time())
                else:
                    binary_time = esp_time


                # INITIAL CLEAN UP (discard extremities)
                # 0 = shorted / floating
                # 4095 = saturated / disconnected
                if not (200 <= raw_adc <= 4094): 
                    continue


                # discard any impossible soil_temp readings 
                if soilTemp_raw <= -55.0 or soilTemp_raw == 85.0:
                    soilTemp_str = ""
                else:
                    soilTemp_str = f"{soilTemp_raw:.2f}"


                # no negative value for Light
                if lightLux_raw < 0:
                    lightLux_str = ""
                else:
                    lightLux_str = f"{lightLux_raw:.2f}"


                # no negative value for Air Temp
                if math.isnan(airTemp_raw) or not (-30.0 <= airTemp_raw <= 40.0):
                    airTemp_str = ""
                else:
                    airTemp_str = f"{airTemp_raw:.2f}"


                # no negative value for Air RH
                if (math.isnan(airRH_raw) or not (0.0 <= airRH_raw <= 100.0)):
                    airRH_str = ""
                else:
                    airRH_str = f"{airRH_raw:.2f}"


                if start_time is None:
                    start_time = time.time()

                elapsed_seconds = round(time.time() - start_time, 2)
                # now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                formatted_row = f"{binary_time},{elapsed_ms},{raw_adc},{soilTemp_str},{lightLux_str},{airTemp_str},{airRH_str}"
                print(formatted_row)
                f.write(formatted_row + "\n")
                f.flush()


    except KeyboardInterrupt:
        print(f"\nLogging stopped. File cleanly saved as {filename}!")
    finally:
        ser.close()


