from pathlib import Path
from src.parser import parse_meta_data_raw

cwd = Path.cwd()


## Parse Meta data to Raw
def generate_meta_data_raw():
    # open the folder,
    folder = cwd / "assets/Markets"
    # loop through each file and pick those with .csv extension
    for file in folder.glob("*.csv"):
        # parse the file
        parse_meta_data_raw(file, cwd / "data/metadata")


if __name__ == "__main__":
    # generate_meta_data_raw()
    generate_meta_data_raw()
