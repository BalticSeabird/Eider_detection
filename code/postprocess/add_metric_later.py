


import pandas as pd
from pathlib import Path

path = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/temp")
output = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/inference/eider_model_nano_v5852/grouped")
files = list(path.rglob("*.csv"))

for file in files: 

    # Read in the file
    out2 = pd.read_csv(file)

    if len(out2) == 0:
        continue

    else: 
    # Group by second
        out2["datetime"] = pd.to_datetime(out2["datetime"])
        grouped_data = out2.groupby([pd.Grouper(key='datetime', freq='2s'), "class"])

        # Aggregate grouped_data (mean confidence score)
        grouped = grouped_data.agg({"conf": "mean", 
                        "frame": "count"}).reset_index()        

        grouped.to_csv(output.joinpath(f'{file.stem}_grouped.csv'), index = False)

