import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the data
data_path = Path("/Users/jonas/Documents/research/seabird/ejder/eider_detection")
files = list(data_path.rglob("*grouped.csv"))

# Compile data files
out = pd.DataFrame()
for file in files:
    temp = pd.read_csv(file)
    temp["station"] = str(file.parent).split("/")[-1]
    out = pd.concat([out, temp])

out = out[["datetime", "class", "counts", "station"]]

d = {"name": ['crow', 'eider_female', 'eider_male', 'gull', 'razorbill'], 
    "class": [0, 1, 2, 3, 4]}
class_id = pd.DataFrame(d)    

out = out.merge(class_id, on = "class")
out["datetime"] = pd.to_datetime(out["datetime"])
out["counts"] = out["counts"].astype("int")
out.sort_values(by = ["datetime"], inplace = True) 

# Plot time series of one station at the time, with datetime as time series and bars of bars for counts
fig, ax = plt.subplots(5, 1)

# Subset data for one station at the time: 
stat = "EJDER6"
dx = out[out["station"] == stat]
plt.suptitle(stat)

for i in range(0, 5):
    dx2 = dx[dx["class"] == (i)]
    ax[i].plot(dx2["datetime"], dx2["counts"]) 
    label = dx2["name"].iloc[0]
    ax[i].annotate(label,
        xy=(0, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize='medium', verticalalignment='top', fontfamily='serif',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
plt.show()