#Version 4: Starting at 0.0s 
import serial
import time
from datetime import datetime

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
    time.sleep(2)  # Wait for serial handshake
    print(f"Connected to ESP32 on {PORT} at {BAUD} baud.")
except Exception as e:
    print(f"Connection error: {e}")
    print("Ensure the PlatformIO Serial Monitor in VS Code is closed!")
    exit(1)


# 3. creating the file
with open(filename, "w", encoding="utf-8") as f:

    # Scientific header for easy plotting
    header = "elapsed_time_s,raw_adc,voltage_v,moisture_pct\n"
    f.write(header)
    f.flush() #forces Python's internal buffer to write the header directly to mac storage disk
    print(f"Logging data to {filename}... Press Ctrl+C to stop.")
    print("-" * 65)

    start_time = None

    try:
        while True:

            # reads the new data bytes and converst to clean Python string 
            raw_line = ser.readline().decode("utf-8", errors="ignore").strip() 

            if not raw_line:
                continue

            # Filter out text headers or boot prints
            if raw_line.startswith("timestamp") or "===" in raw_line or "ESP32" in raw_line:
                continue


            # Time normalization aka, start at 0s
            parts = raw_line.split(",")

            # Expecting 4 values from firmware: millis, raw_adc, voltage, moisture_pct
            if len(parts) == 4:
                if start_time is None:
                    start_time = time.time()

                elapsed_seconds = round(time.time() - start_time, 2)
                # now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                raw_adc = parts[1]
                voltage = parts[2]
                moisture_pct = parts[3]

                # formatted_row = f"{now_str},{elapsed_seconds},{raw_adc},{voltage},{moisture_pct}"
                formatted_row = f"{elapsed_seconds},{raw_adc},{voltage},{moisture_pct}"
                print(formatted_row)
                f.write(formatted_row + "\n")
                f.flush()


    except KeyboardInterrupt:
        print(f"\nLogging stopped. File cleanly saved as {filename}!")
    finally:
        ser.close()



# Version 1:
# import serial
# import time

# # Set port and baud rate
# PORT = "/dev/cu.usbserial-0001"  # Adjust to your port name
# BAUD = 115200

# ser = serial.Serial(PORT, BAUD, timeout=2)
# time.sleep(2)  # Wait for connection to settle

# with open("soil_data.csv", "w", encoding="utf-8") as f:
#     print("Logging data to soil_data.csv... Press Ctrl+C to stop.")
#     try:
#         while True:
#             line = ser.readline().decode('utf-8', errors='ignore').strip()
#             if line:
#                 print(line)
#                 f.write(line + "\n")
#                 f.flush()
#     except KeyboardInterrupt:
#         print("\nLogging stopped. File saved as soil_data.csv!")
#     finally:
#         ser.close()


# # Version 2:
# import serial
# import time

# # Set port and baud rate
# PORT = "/dev/cu.usbserial-0001"  # Adjust to your port name
# BAUD = 115200

# ser = serial.Serial(PORT, BAUD, timeout=2)
# time.sleep(2)  # Wait for connection to settle

# with open("soil_data_water.csv", "w", encoding="utf-8") as f:
#     print("Logging data to soil_data_water.csv... Press Ctrl+C to stop.")
#     try:
#         while True:
#             line = ser.readline().decode('utf-8', errors='ignore').strip()
#             if line:
#                 print(line)
#                 f.write(line + "\n")
#                 f.flush()
#     except KeyboardInterrupt:
#         print("\nLogging stopped. File saved as soil_data_water.csv!")
#     finally:
#         ser.close()

# Version 3
# import serial
# import time

# # Set port and baud rate
# PORT = "/dev/cu.usbserial-0001"  # Adjust to your port name
# BAUD = 115200

# # Prompt for custom file name
# custom_name = input("Enter file name : ").strip()

# # Append .csv if not typed, or fall back to default
# if not custom_name:
#     filename = "test_run.csv"
# elif not custom_name.endswith(".csv"):
#     filename = f"{custom_name}.csv"
# else:
#     filename = custom_name

# ser = serial.Serial(PORT, BAUD, timeout=2)
# time.sleep(2)  # Wait for connection to settle

# with open(filename, "w", encoding="utf-8") as f:
#     print(f"Logging data to {filename}... Press Ctrl+C to stop.")
#     try:
#         while True:
#             line = ser.readline().decode('utf-8', errors='ignore').strip()
#             if line:
#                 print(line)
#                 f.write(line + "\n")
#                 f.flush()
#     except KeyboardInterrupt:
#         print(f"\nLogging stopped. File saved as {filename}!")
#     finally:
#         ser.close()