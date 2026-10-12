
import pandas as pd

# extracting from in_water2.cvs
df = pd.read_csv("/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/in_water.csv")
cols = ["time_ms", "raw_adc", "voltage_v"]
df = df.drop_duplicates(subset="time_ms") #removing the intiial measurements that are the same 


# df = pd.read_csv("/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/in_water2.csv")
# cols = ["elapsed_time_s", "raw_adc", "voltage_v", "moisture_pct"]
# df = df.drop_duplicates(subset="elapsed_time_s") #removing the intiial measurements that are the same 



n = len(df)
mean = df["raw_adc"].mean()
std = df["raw_adc"].std()
sem = std / n**0.5
print(f"N={n}  mean={mean:.3f}  std={std:.4f}  SEM={sem:.4f}  median={df['raw_adc'].median():.3f}")


n = len(df)
mean_voltage = df["voltage_v"].mean()
std_voltage = df["voltage_v"].std()
sem_voltage = std_voltage / n**0.5
print(f"N={n}  mean={mean_voltage:.3f}  std={std_voltage:.4f}  SEM={sem_voltage:.4f}  median={df['voltage_v'].median():.4f}")

# results
# N=81  mean=952.9  std=24.7  SEM=2.75  median=951
# N=81  mean=0.769  std=0.0204  SEM=0.0023  median=0.770