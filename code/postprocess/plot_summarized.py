import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys 

# Plot time series of one station at the time, with datetime as time series and bars of bars for counts
fig, ax = plt.subplots(5, 1)

# Read data
out = pd.read_csv("data/compiled_nanov5852_v3.csv")

# Subset data for one station at the time: 
stat = sys.argv[1]
out = out[out["station"] == stat]
out["datetime"] = pd.to_datetime(out["datetime"])



plt.suptitle(stat)

for i in range(0, 5):
    dx2 = out[out["class"] == (i)]
    
    dx2 = dx2.drop_duplicates(subset='datetime')

    # Subset based on confidence level
    dx2 = dx2[dx2["conf"] > 0.3]

    # Full date time sequence
    date_rng = pd.date_range(start=dx2["datetime"].min(), end=dx2["datetime"].max(), freq='2S')

    # Fill missing values
    dx2 = dx2.set_index('datetime').reindex(date_rng, fill_value=0).reset_index().rename(columns={'index': 'datetime'})

    # Create a new y series which is a 10 point running mean of the original y series
    y = dx2["frame"]/50
    y_rolling = y.rolling(window=10).mean()

    ax[i].plot(dx2["datetime"], y, c = "red", alpha = 0.4)
    ax[i].plot(dx2["datetime"], y_rolling, color = "black", alpha = 0.9) 

    label = dx2["name"].iloc[0]
    ax[i].annotate(label,
        xy=(0, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
plt.show()

""" 
# Alternative
fig, ax = plt.subplots(1, 1)

# Subset data for one station at the time: 
dx = out[out["station"] == stat]
plt.suptitle(stat)
cols = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
xs = [0, .2, .4, .6, .8]
for i in range(0, 5):
    dx2 = dx[dx["class"] == (i)]
    ax.plot(dx2["datetime"], dx2["counts"]/50, color = cols[i]) 
    label = dx2["name"].iloc[0]
    ax.annotate(label,
        xy=(xs[i], 1), xycoords='axes fraction', color = cols[i],
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
plt.show()
 """