# import pandas as pd
# import matplotlib.pyplot as plt

# # 1. Load the data
# df = pd.read_csv("Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/ambient_air.csv")

# # 2. Basic cleanup: make sure columns are numeric, drop rows that failed to parse
# # (forcing every column to numbers and dropping any broken rows. )

# cols = ["elapsed_time_s", "raw_adc", "voltage_v", "moisture_pct"]
# df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")
# df = df.dropna(subset=cols)

# # 3. Convert seconds to hours so the x-axis is readable for an overnight run
# # raw lines stays in gray (aka real data)
# # df["hours"] = df["elapsed_time_s"] / 3600
# df["minutes"] = df["elapsed_time_s"] / 60

# # 4. Smooth the moisture signal to reduce sensor noise 
# # aka rolling median over 15 samples to remove any data spikes
# df["moisture_smooth"] = df["moisture_pct"].rolling(15, center=True, min_periods=1).median()
# df["voltage_smooth"] = df["voltage_v"].rolling(15, center=True, min_periods=1).median()
# df["raw_adc_smooth"] = df["raw_adc"].rolling(15, center=True, min_periods=1).median()

# # 5. Two stacked panels sharing the same time axis
# # top shows moisture percent over time, which is the main graph.
# # fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
# fig, (ax1) = plt.subplots(1, 1, figsize=(11, 9), sharex=True)



# # Top plot "Moisture over elapsed time"
# ax1.plot(df["minutes"], df["moisture_pct"], color="lightgray", label="Raw Moisture Content") # make the raw data in grey
# ax1.plot(df["minutes"], df["moisture_smooth"], color="tab:green", label="Filtered Moisture Content") # let green be the smoothed out data

# ax1.set_ylabel("Moisture (%)")
# ax1.set_title("Apparent Volumetric Moisture Content Over Time (min)")
# ax1.legend()
# ax1.grid(alpha=0.3) # make the grid lines 0.3 opaque


# # # Middle Plot "Voltage over elapsed time"
# # ax2.plot(df["minutes"], df["voltage_v"], color="lightgray", label="Raw Voltage") # make the raw data in grey
# # ax2.plot(df["minutes"], df["voltage_smooth"], color="tab:blue", label="Filtered Voltage Signal") # let green be the smoothed out data

# # ax2.set_ylabel("Voltage (V)")
# # ax2.set_title("Sensor Analog Signal (Vout) Over Time (min)")
# # ax2.legend()
# # ax2.grid(alpha=0.3) 



# # # Bottom Plot "Voltage over elapsed time"
# # ax3.plot(df["minutes"], df["raw_adc"], color="lightgray", label="Raw ADC counts") # make the raw data in grey
# # ax3.plot(df["minutes"], df["raw_adc_smooth"], color="tab:purple", label="Filtered ADC counts") # let green be the smoothed out data

# # ax3.set_ylabel("Raw ADC")
# # ax3.set_title("ESP32 ADC Count Over Time (min)")
# # ax3.legend()
# # ax3.set_xlabel("Elapsed time (minutes)")
# # ax3.grid(alpha=0.3) 



# # # ax2.plot(df["hours"], df["voltage_v"], color="tab:blue", label="Voltage (V)")
# # # ax2.set_ylabel("Voltage (V)", color="tab:blue")
# # # ax2.set_xlabel("Elapsed time (hours)")
# # # ax2.grid(alpha=0.3) 



# # # ax2b = ax2.twinx()  # second y-axis for the raw ADC counts
# # # ax2b.plot(df["hours"], df["raw_adc"], color="tab:orange", alpha=0.6, label="Raw ADC")
# # # ax2b.set_ylabel("Raw ADC", color="tab:orange")


# plt.tight_layout()
# plt.savefig("ambient_air", dpi=150)
# print(f"Plot saved successfully")
# plt.show()


import pandas as pd

# df = pd.read_csv("/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/ambient_air.csv", header=None,
#                  names=["time_ms", "raw_adc", "voltage_v"])


df = pd.read_csv("/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/ambient_air.csv")
cols = ["time_ms", "raw_adc", "voltage_v"]
df = df.drop_duplicates(subset="time_ms") #removing the intiial measurements that are the same 



# # drop the first 30 s while the sensor settles
# t0 = df["time_ms"].iloc[0]
# df = df[df["time_ms"] > t0 + 30_000]


n = len(df)
mean = df["raw_adc"].mean()
std = df["raw_adc"].std()
sem = std / n**0.5
print(f"N={n}  mean={mean:.1f}  std={std:.1f}  SEM={sem:.2f}  median={df['raw_adc'].median():.0f}")


n = len(df)
mean_voltage = df["voltage_v"].mean()
std_voltage = df["voltage_v"].std()
sem_voltage = std_voltage / n**0.5
print(f"N={n}  mean={mean_voltage:.3f}  std={std_voltage:.4f}  SEM={sem_voltage:.4f}  median={df['voltage_v'].median():.3f}")


# Results !!!
# N=49  mean=2637.2  std=37.9  SEM=5.41  median=2643






# n = len(df)
# adc_mean = df["raw_adc"].mean()
# adc_std = df["raw_adc"].std()
# adc_sem = adc_std / n**0.5

# v_mean = df["voltage_v"].mean()
# v_std = df["voltage_v"].std()



# N = 19 samples over 18 s
# Air ADC = 2636.6 ± 35.2 (std), SEM 8.07

# std: scatter of inidividual readings, descibe how noisy the sensor is 
    # "how noisy is one reading"
# SEM: standard error over mean => how weel you know the average (std/sqrt(19))
    # each measurements is noisy, but taking the "average of error" diminishes the errors
    # "how precisely do i know the average air value"




# Air voltage = 2.125 ± 0.028 V (std)