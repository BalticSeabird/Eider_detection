import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys 

# Plot time series of one station at the time, with datetime as time series and bars of bars for counts
fig, ax = plt.subplots(5, 1)

# Read data
out = pd.read_csv("data/compiled2sV2.csv")
out["datetime"] = pd.to_datetime(out["datetime"])

# Subset data for one station at the time: 
stat = sys.argv[1]

dx = out[out["station"] == stat]
plt.suptitle(stat)

for i in range(0, 5):
    dx2 = dx[dx["class"] == (i)]
    ax[i].plot(dx2["datetime"], dx2["counts"]/50) 
    label = dx2["name"].iloc[0]
    ax[i].annotate(label,
        xy=(0, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
plt.show()


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
