
from pathlib import Path
import shutil

# Define input and output folders
input_folder = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/inference")
output_folder = Path("../../../../../../mnt/BSP_NAS2_work/eider_model/temp")

files = list(input_folder.rglob("*grouped.csv"))

# Loop through all files in the input folder
for file in files: 
    # Copy to the output folder
    outname = output_folder.joinpath(file.name)
    shutil.copy(file, outname)
    print(f"File {file} copied to {outname}")
