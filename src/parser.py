from pathlib import Path
import pandas as pd


file_name = "Bond"
file_path = f"raw/{file_name}.txt"
# read the text file into a dataframe
df = pd.read_csv(file_path, sep="\t")
df.to_csv(f"csv/{file_name}.csv", index=False)


def parse_txt_to_csv(file_path: Path | str, seperator: str = "\t"):
    """Parse a text file into a csv file.

    Args:
        file_path (str or Path): The path to the text file.
    """
    # read the text file into a dataframe
    df = pd.read_csv(file_path, sep=seperator)
    # output files to csv folder
    df.to_csv(f"csv/{file_name}.csv", index=False)
