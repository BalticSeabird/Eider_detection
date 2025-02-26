
import pandas as pd
from pathlib import Path


# Read folders 
data_path = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/inference/eider_model_nano_v5852/grouped")
files = list(data_path.rglob("*grouped.csv"))

# Compile data files
out = pd.DataFrame()
for file in files:
    temp = pd.read_csv(file)
    temp["station"] = file.name.split("_")[-4]
    #temp["station"] = str(file.parent).split("/")[-1]
    out = pd.concat([out, temp])
    print(file.name)

out = out[["datetime", "class", "conf", "frame", "station"]]

d = {"name": ['crow', 'eider_female', 'eider_male', 'gull', 'razorbill'], 
    "class": [0, 1, 2, 3, 4]}
class_id = pd.DataFrame(d)    

out = out.merge(class_id, on = "class")
out["counts"] = out["frame"].astype("int")

out["datetime"] = pd.to_datetime(out["datetime"], format = "mixed")

out.sort_values(by = ["station", "datetime"], inplace = True) 

out.to_csv("data/compiled_nanov5852_v2.csv", index = False)