from pathlib import Path
from src.parser import parse_meta_data_raw, combine_csv

cwd = Path.cwd()


## Parse Meta data to Raw
def generate_meta_data_raw():
    # open the folder,
    folder = cwd / "assets/Markets"
    # loop through each file and pick those with .csv extension
    for file in folder.glob("*.csv"):
        # parse the file
        parse_meta_data_raw(file, cwd / "data/metadata")


## unify the data into one file
def generate_meta_data():
    combine_csv(cwd / "data/metadata", cwd / "data/metadata")


if __name__ == "__main__":
    # step 1: generate_meta_data_raw()
    # generate_meta_data_raw()
    # step 2: generate_meta_data()
    generate_meta_data()
