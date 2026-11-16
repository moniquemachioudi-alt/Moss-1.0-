"""
Quick developer tool: plot Moss sensor readings over time with trendlines.

Run from the moss-backend folder (where your .env lives), with (moss) active:
    pip install pandas matplotlib
    python plot_readings.py
"""
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()  # reads SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY from .env
supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_ROLE_KEY"],
)

DEVICE = "esp32_01"
COLUMNS = ["soil_moisture_pct", "soil_temp_c", "light_lux", "air_temp_c", "air_rh_pct"]
ROLLING_WINDOW = 5  # points in the moving average

# Newest 1000 rows (Supabase returns at most 1000 per request by default)
resp = (
    supabase.table("readings")
    .select("*")
    .eq("device_id", DEVICE)
    .order("recorded_at", desc=True)
    .limit(1000)
    .execute()
)

if not resp.data:
    raise SystemExit(f"No readings found for device {DEVICE!r}.")

df = pd.DataFrame(resp.data)
df["recorded_at"] = pd.to_datetime(df["recorded_at"])
df = df.sort_values("recorded_at")  # oldest to newest for plotting

fig, axes = plt.subplots(
    len(COLUMNS), 1, sharex=True, figsize=(10, 2.6 * len(COLUMNS))
)

for ax, col in zip(axes, COLUMNS):
    if col not in df.columns:
        ax.set_ylabel(col)
        ax.text(0.5, 0.5, "column not in table", ha="center", transform=ax.transAxes)
        continue

    s = df[["recorded_at", col]].dropna()
    ax.set_ylabel(col)
    if s.empty:
        ax.text(0.5, 0.5, "no data", ha="center", transform=ax.transAxes)
        continue

    # The measurements themselves
    ax.plot(s["recorded_at"], s[col], marker=".", linestyle="-", alpha=0.5, label="readings")

    # Moving average: smooths noise
    ax.plot(
        s["recorded_at"],
        s[col].rolling(ROLLING_WINDOW, min_periods=1).mean(),
        linewidth=2,
        label=f"moving avg ({ROLLING_WINDOW})",
    )

    # Linear trend: fitted straight line (needs at least 2 points)
    if len(s) >= 2:
        t = (s["recorded_at"] - s["recorded_at"].min()).dt.total_seconds()
        slope, intercept = np.polyfit(t, s[col], 1)
        ax.plot(s["recorded_at"], slope * t + intercept, linestyle="--", label="linear trend")

    ax.legend(loc="upper right", fontsize=8)

axes[-1].set_xlabel("time")
fig.suptitle(f"Moss readings: {DEVICE}")
fig.tight_layout()
plt.show()