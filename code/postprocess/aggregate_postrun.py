


import pandas as pd
from pathlib import Path

path = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/inference/2024/eider_model_nano_v5852/2024")
#output = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/inference/eider_model_nano_v5852/grouped")
files = list(path.rglob("*raw.csv"))

for file in files: 

    # Read in the file
    out2 = pd.read_csv(file, parse_dates = ["datetime"])
    outname = file.parent.joinpath(f'{file.stem[0:-3]}_grouped5s.csv')

    if len(out2) == 0:
        continue

    else: 
        print(f'processing... {file.stem}')
        grouped_data = out2.groupby([pd.Grouper(key='datetime', freq='5s'), "class"])

        # Aggregate grouped_data (mean confidence score)
        grouped = grouped_data.agg({"conf": "mean", 
                        "frame": "count"}).reset_index()        

        grouped.to_csv(outname, index = False)

