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
import serial
import time

# Set port and baud rate
PORT = "/dev/cu.usbserial-0001"  # Adjust to your port name
BAUD = 115200

# Prompt for custom file name
custom_name = input("Enter file name : ").strip()

# Append .csv if not typed, or fall back to default
if not custom_name:
    filename = "test_run.csv"
elif not custom_name.endswith(".csv"):
    filename = f"{custom_name}.csv"
else:
    filename = custom_name

ser = serial.Serial(PORT, BAUD, timeout=2)
time.sleep(2)  # Wait for connection to settle

with open(filename, "w", encoding="utf-8") as f:
    print(f"Logging data to {filename}... Press Ctrl+C to stop.")
    try:
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print(line)
                f.write(line + "\n")
                f.flush()
    except KeyboardInterrupt:
        print(f"\nLogging stopped. File saved as {filename}!")
    finally:
        ser.close()