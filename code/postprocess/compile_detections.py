
import pandas as pd
from pathlib import Path


# Read folders 
data_path = Path("data/nano_v5852/grouped")
files = list(data_path.rglob("*grouped.csv"))

# Compile data files
out = pd.DataFrame()
for file in files:
    temp = pd.read_csv(file)
    temp["station"] = file.name.split("_")[-4]
    temp.rename(columns = {"datetime": "datetime", "class": "class", "conf": "conf", "frame": "counts"}, inplace = True)
    out = pd.concat([out, temp])
    print(file.name)

out = out[["datetime", "class", "conf", "counts", "station"]]

d = {"name": ['crow', 'eider_female', 'eider_male', 'gull', 'razorbill'], 
    "class": [0, 1, 2, 3, 4]}
class_id = pd.DataFrame(d)    

out = out.merge(class_id, on = "class")

out["datetime"] = pd.to_datetime(out["datetime"], format = "mixed")

out.sort_values(by = ["station", "datetime"], inplace = True) 

out.to_csv("data/compiled_nanov5852_v4.csv", index = False)