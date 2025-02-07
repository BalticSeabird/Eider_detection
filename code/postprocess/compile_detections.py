
import pandas as pd
from pathlib import Path


# Read folders 
data_path = Path("data/grouped/")
files = list(data_path.rglob("*.csv"))

# Compile data files
out = pd.DataFrame()
for file in files:
    temp = pd.read_csv(file)
    temp["station"] = file.name.split("_")[-4]
    #temp["station"] = str(file.parent).split("/")[-1]
    out = pd.concat([out, temp])
    print(file.name)

out = out[["datetime", "class", "counts", "station"]]

d = {"name": ['crow', 'eider_female', 'eider_male', 'gull', 'razorbill'], 
    "class": [0, 1, 2, 3, 4]}
class_id = pd.DataFrame(d)    

out = out.merge(class_id, on = "class")
out["datetime"] = pd.to_datetime(out["datetime"])
out["counts"] = out["counts"].astype("int")
out.sort_values(by = ["datetime"], inplace = True) 

out.to_csv("data/compiled2sV2.csv", index = False)