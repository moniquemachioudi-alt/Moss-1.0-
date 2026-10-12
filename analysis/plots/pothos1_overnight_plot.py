# import os
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # 1. Load the data
# csv_path = "/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/pothos1_overnight.csv"
# df = pd.read_csv(csv_path)

# # 2. Enforce numeric types and drop parsing artifacts
# cols = ["elapsed_time_s", "raw_adc", "voltage_v", "moisture_pct"]
# df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")
# df = df.dropna(subset=cols)

# # 3. Time scale: convert seconds to hours for a readable multi-hour diurnal axis
# df["hours"] = df["elapsed_time_s"] / 3600.0

# # 4. Outlier Rejection: isolate hardware dropouts (intermittent loose jumper / oscillator stalls)
# # In potting soil, ADC cannot physically drop below 500 without immersion in pure liquid
# valid_mask = (df["raw_adc"] > 500) & (df["voltage_v"] > 0.35)

# df_clean = df.copy()
# df_clean.loc[~valid_mask, ["raw_adc", "voltage_v", "moisture_pct"]] = np.nan
# df_clean = df_clean.interpolate(method="linear")

# # 5. Dual-Stage Filter:
# # 60-sample rolling median rejects single-point impulse noise,
# # followed by 30-sample rolling mean to eliminate Gaussian ADC quantization jitter
# window_median = 60
# window_mean = 30

# df_clean["moisture_smooth"] = (
#     df_clean["moisture_pct"]
#     .rolling(window_median, min_periods=1)
#     .median()
#     .rolling(window_mean, min_periods=1)
#     .mean()
# )
# df_clean["voltage_smooth"] = (
#     df_clean["voltage_v"]
#     .rolling(window_median, min_periods=1)
#     .median()
#     .rolling(window_mean, min_periods=1)
#     .mean()
# )
# df_clean["adc_smooth"] = (
#     df_clean["raw_adc"]
#     .rolling(window_median, min_periods=1)
#     .median()
#     .rolling(window_mean, min_periods=1)
#     .mean()
# )

# # 6. Publication Figure Layout (3 Panels, shared hours x-axis)
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(5, 5), sharex=True, dpi=300)

# # (a) Moisture Subplot
# ax1.plot(
#     df["hours"],
#     df["moisture_pct"],
#     color="#d6d6d6",
#     alpha=0.6,
#     label="Raw Telemetry (1 Hz)",
# )
# ax1.plot(
#     df_clean["hours"],
#     df_clean["moisture_smooth"],
#     color="#2e7d32",
#     linewidth=1.8,
#     label="Filtered (Artifacts Rejected)",
# )
# ax1.set_ylabel("Moisture Content (%)", fontweight="bold", fontsize=10)
# ax1.set_title(
#     "(a) Apparent Volumetric Moisture Content ($\theta$)",
#     loc="left",
#     fontweight="bold",
#     fontsize=11,
# )
# ax1.set_ylim(0, 100)
# ax1.legend(loc="upper right", frameon=True, fontsize=9)
# ax1.grid(alpha=0.3)

# # (b) Voltage Subplot
# ax2.plot(
#     df["hours"],
#     df["voltage_v"],
#     color="#d6d6d6",
#     alpha=0.6,
#     label="Raw Signal",
# )
# ax2.plot(
#     df_clean["hours"],
#     df_clean["voltage_smooth"],
#     color="#0277bd",
#     linewidth=1.8,
#     label="Filtered Signal ($V_{\mathrm{out}}$)",
# )
# ax2.set_ylabel("Sensor Signal (V)", fontweight="bold", fontsize=10)
# ax2.set_title(
#     "(b) Analog Output Potential ($V_{\mathrm{out}}$)",
#     loc="left",
#     fontweight="bold",
#     fontsize=11,
# )
# ax2.legend(loc="upper right", frameon=True, fontsize=9)
# ax2.grid(alpha=0.3)

# # (c) ADC Counts Subplot
# ax3.plot(
#     df["hours"],
#     df["raw_adc"],
#     color="#d6d6d6",
#     alpha=0.6,
#     label="Raw ADC Counts",
# )
# ax3.plot(
#     df_clean["hours"],
#     df_clean["adc_smooth"],
#     color="#7b1fa2",
#     linewidth=1.8,
#     label="Filtered ADC Counts",
# )
# ax3.set_ylabel("ADC Value (12-bit)", fontweight="bold", fontsize=10)
# ax3.set_xlabel("Elapsed Time (Hours)", fontweight="bold", fontsize=10)
# ax3.set_title(
#     "(c) ESP32 ADC1 Quantization (GPIO 34)",
#     loc="left",
#     fontweight="bold",
#     fontsize=11,
# )
# ax3.legend(loc="upper right", frameon=True, fontsize=9)
# ax3.grid(alpha=0.3)

# plt.tight_layout()
# output_img = "pothos1_overnight_cleaned.png"
# plt.savefig(output_img, dpi=300)
# print(f"Plot saved successfully as {output_img}")
# plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

csv_path = "/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/pothos1_overnight.csv"
df = pd.read_csv(csv_path)

cols = ["elapsed_time_s", "raw_adc", "voltage_v", "moisture_pct"]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=cols).reset_index(drop=True)
df["hours"] = df["elapsed_time_s"] / 3600.0

# Outlier rejection: hardware dropouts (ADC/voltage railing to ~0)
valid = (df["raw_adc"] > 500) & (df["voltage_v"] > 0.35)
n_bad = (~valid).sum()
print(f"Rejected {n_bad} of {len(df)} samples ({100 * n_bad / len(df):.2f}%)")

clean = df.copy()
clean.loc[~valid, ["raw_adc", "voltage_v", "moisture_pct"]] = np.nan  # no interpolation

# Dual-stage filter (centred): rolling median -> rolling mean
W_MED, W_MEAN = 60, 30
def smooth(s):
    return (s.rolling(W_MED, center=True, min_periods=W_MED // 4).median()
             .rolling(W_MEAN, center=True, min_periods=W_MEAN // 4).mean())

panels = [
    ("moisture_pct", "#2e7d32", "Moisture (%)",
     "Raw Moisture Content", "Filtered Moisture Content",
     "(a) Apparent Volumetric Moisture Content Over Time (h)", "upper right"),
    ("voltage_v", "#0277bd", r"$V_{\mathrm{out}}$ (V)",
     "Raw Voltage", r"Filtered Voltage Signal ($V_{\mathrm{out}}$)",
     r"(b) Sensor Analog Signal ($V_{\mathrm{out}}$) Over Time (h)", "lower right"),
    ("raw_adc", "#7b1fa2", "ADC (counts)",
     "Raw ADC Counts", "Filtered ADC Counts",
     "(c) ESP32 ADC Count Over Time (h)", "lower right"),
]

fig, axes = plt.subplots(3, 1, figsize=(6.5, 7.5), sharex=True)
for ax, (col, color, ylabel, raw_label, filt_label, title, leg_loc) in zip(axes, panels):
    ax.plot(clean["hours"], clean[col], color="#c8c8c8", lw=0.6, label=raw_label)
    ax.plot(clean["hours"], smooth(clean[col]), color=color, lw=1.4, label=filt_label)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_title(title, fontsize=9)
    ax.grid(alpha=0.3)
    ax.tick_params(labelsize=8)
    ax.legend(loc=leg_loc, frameon=True, fontsize=7)

axes[-1].set_xlabel("Elapsed time (hours)", fontsize=9)
axes[-1].xaxis.set_major_locator(MultipleLocator(2))

plt.tight_layout()
plt.savefig("pothos1_overnight_cleaned.png", dpi=300, bbox_inches="tight")
plt.show()