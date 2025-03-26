
import pandas as pd
from pathlib import Path


# Read folders 
data_path = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/inference/2024/eider_model_nano_v5852/2024")
files = list(data_path.rglob("*grouped5s.csv"))

# Compile data files
out = pd.DataFrame()
for file in files:
    temp = pd.read_csv(file)
    temp["station"] = file.name.split("_")[-5]
    temp.rename(columns = {"datetime": "datetime", "class": "class", "conf": "conf", "frame": "counts"}, inplace = True)
    out = pd.concat([out, temp])
    print(f'compiling ... {file.name}')

out = out[["datetime", "class", "conf", "counts", "station"]]

d = {"name": ['crow', 'eider_female', 'eider_male', 'gull', 'razorbill'], 
    "class": [0, 1, 2, 3, 4]}
class_id = pd.DataFrame(d)    

out = out.merge(class_id, on = "class")

out["datetime"] = pd.to_datetime(out["datetime"], format = "mixed")

out.sort_values(by = ["station", "datetime"], inplace = True) 

out.to_csv("../../../../../../mnt/BSP_NAS2_work/eider_model/inference/eider2024_nanov5852_v5.csv", index = False)

print(f'example rows: {out.head()}')