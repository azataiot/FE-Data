from pathlib import Path
import pandas as pd

# get a list of .txt files located in the raw directory using python's pathlib module
file_list = [f for f in Path("raw").glob("*.txt")]


file_list = ["raw/bond.txt"]
# parse dataframe from each text file
# for file_name in file_list:
#     # read the text file into a dataframe
#     df = pd.read_csv(file_name, sep="\t")
#     # output files to csv folder
#     df.to_csv(f"csv/{file_name}.csv", index=False)


file_name = "Bond"
file_path = f"raw/{file_name}.txt"
# read the text file into a dataframe
df = pd.read_csv(file_path, sep="\t")
df.to_csv(f"csv/{file_name}.csv", index=False)
