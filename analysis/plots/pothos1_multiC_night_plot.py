import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FuncFormatter

# 1. Load already-cleaned Supabase CSV export
csv_path = "/Users/linyunlei/Documents/mySideQuests/Moss/Code/Moss-1.0-/analysis/data/raw/SQL_pothos1_multiC_night.csv"  # <-- Update path to your CSV
df = pd.read_csv(csv_path)

# 2. Parse UTC timestamps -> Montreal local time & elapsed hours (starting at 0.0 h)
df["recorded_at"] = pd.to_datetime(df["recorded_at"], utc=True, errors="coerce")
df = df.dropna(subset=["recorded_at"]).sort_values("recorded_at").reset_index(drop=True)
df["local_time"] = df["recorded_at"].dt.tz_convert("America/Montreal")
df["hours"] = (df["recorded_at"] - df["recorded_at"].iloc[0]).dt.total_seconds() / 3600.0

t0_local = df["local_time"].iloc[0]

# 3. Dual-stage centered smoothing (~1 min window for ~6–7s sampling)
W_MED, W_MEAN = 9, 5
def smooth(s):
    return (
        s.rolling(W_MED, center=True, min_periods=1).median()
         .rolling(W_MEAN, center=True, min_periods=1).mean()
    )

# 4. Create 3-panel multi-sensor poster figure
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7.5, 8.0), sharex=True, dpi=300)

# --- Panel (a): Substrate Moisture (%) ---
ax1.plot(df["hours"], df["soil_moisture_pct"], color="#c8c8c8", lw=0.8, label="Raw Telemetry")
ax1.plot(df["hours"], smooth(df["soil_moisture_pct"]), color="#2e7d32", lw=1.8, label="Filtered Moisture (%)")
ax1.set_ylabel("Soil Moisture (%)", fontsize=9.5, fontweight="bold", color="#2e7d32")
ax1.set_title("(a) Calibrated Substrate Moisture Content", loc="left", fontsize=10, fontweight="bold")
ax1.grid(alpha=0.3)
ax1.legend(loc="upper center", ncol=2, frameon=True, fontsize=8)

# --- Panel (b): Soil Temperature & Air Temperature (°C) ---
ax2.plot(df["hours"], smooth(df["soil_temp_c"]), color="#d84315", lw=1.8, label="Substrate Temp (°C)")
ax2.plot(df["hours"], smooth(df["air_temp_c"]), color="#0277bd", lw=1.6, linestyle="--", label="Canopy Air Temp (°C)")
ax2.set_ylabel("Temperature (°C)", fontsize=9.5, fontweight="bold", color="#0277bd")
ax2.set_title("(b) Coupled Root-Zone & Canopy Thermal Dynamics", loc="left", fontsize=10, fontweight="bold")
ax2.grid(alpha=0.3)
ax2.legend(loc="upper center", ncol=2, frameon=True, fontsize=8)


rh_smooth = (
    df["air_rh_pct"]
    .rolling(25, center=True, min_periods=1).median()
    .rolling(15, center=True, min_periods=1).mean()
)

# --- Panel (c): Ambient Light (Lux) & Relative Humidity (%) ---
ax3_rh = ax3.twinx()
l1, = ax3.plot(df["hours"], smooth(df["light_lux"]), color="#f9a825", lw=1.8, label="Ambient Light (lux)")
# l2, = ax3_rh.plot(df["hours"], smooth(df["air_rh_pct"]), color="#6a1b9a", lw=1.6, linestyle="-.", label="Relative Humidity (%)")
l2, = ax3_rh.plot(
    df["hours"],
    rh_smooth,
    color="#6a1b9a",
    lw=1.8,
    linestyle="-.",
    label="Relative Humidity (%)",
)

ax3.set_ylabel("Light Intensity (lux)", fontsize=9.5, fontweight="bold", color="#e65100")
ax3_rh.set_ylabel("Air RH (%)", fontsize=9.5, fontweight="bold", color="#6a1b9a")
ax3_rh.set_ylim(74, 84)
ax3.set_title("(c) Canopy Light Flux & Atmospheric Humidity", loc="left", fontsize=10, fontweight="bold")
ax3.grid(alpha=0.3)
ax3_rh.grid(False)
ax3.legend(
    [l1, l2],
    ["Ambient Light (lux)", "Relative Humidity (%)"],
    loc="upper center",
    ncol=2,            # Puts both labels side-by-side in one compact bar
    frameon=True,
    fontsize=8,
)

# --- Stacked Bottom X-Axis: Elapsed Hours + Local Clock Time Underneath ---
def format_dual_time(x, pos):
    if x < 0:
        return ""
    clock_str = (t0_local + pd.Timedelta(hours=float(x))).strftime("%H:%M")
    hour_str = f"{x:g} h"
    return f"{hour_str}\n({clock_str})"

ax3.xaxis.set_major_formatter(FuncFormatter(format_dual_time))
ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.set_xlabel("Elapsed Time / Local Clock Time (EST)", fontsize=9.5, fontweight="bold", labelpad=6)

for ax in (ax1, ax2, ax3):
    ax.tick_params(labelsize=8.5)

plt.tight_layout()
plt.savefig("pothos1_multiC_night_plot.png", dpi=300, bbox_inches="tight")
plt.show()