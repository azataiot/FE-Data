from pathlib import Path
import pandas as pd
from .utility import file_exists, extract_df_columns


def parse_txt_to_csv(file_path: Path | str, seperator: str = "\t"):
    """Parse a text file into a csv file.

    Args:
        file_path (str or Path): The path to the text file.
    """
    # read the text file into a dataframe
    df = pd.read_csv(file_path, sep=seperator)
    # output files to csv folder
    df.to_csv(f"csv/{file_path}.csv", index=False)


def parse_meta_data_raw(file_path: Path | str, output_path: Path | str):
    """Parse a csv file into df and save as csv.

    Args:
        file_path (str or Path): The path to the csv file.
    """
    # check the csv file exists
    if not file_exists(file_path):
        raise FileNotFoundError(f"File not found at {file_path}")

    # read the csv file into a dataframe
    df = pd.read_csv(file_path)

    # extract the columns we need
    df = extract_df_columns(
        df,
        column_names=["Symbol", "Name"],
        new_column_names=["symbol", "name"],
    )

    # as the Crypto.csv file has some problems on the symbol column, we need to fix it manually
    # Bitcoin USDBTC-USD,Bitcoin USD,"28,034.45",121.82,+0.44%,542.201B,9.404B,9.404B,9.404B,19.341M,,
    # it Should be like this: BTC-USD,Bitcoin USD,"28,034.45",121.82,+0.44%,542.201B,9.404B,9.404B,9.404B,19.341M,,
    # first we need to strip the first column content, then the fixed symbol = first column - second column (string)

    def strip_symbol(row):
        symbol = row["symbol"].strip()
        name = row["name"].strip()
        if symbol.startswith(name):
            symbol = symbol[len(name) :]
        return symbol

    if Path(file_path).stem == "Crypto":
        df["symbol"] = df.apply(strip_symbol, axis=1)

    # add new column 'market' with vaule as the file name without extension
    df["market"] = Path(file_path).stem
    # output files to csv folder
    out_put_file = Path(output_path) / f"{Path(file_path).stem}.csv"
    df.to_csv(out_put_file, index=False)


def combine_csv(input_path: Path | str, output_path: Path | str):
    """Combine all csv files in a folder into one csv file.

    Args:
        input_path (str or Path): The path to the folder.
        output_path (str or Path): The path to the output csv file.
    """
    # read the csv file into a dataframe
    df = pd.concat([pd.read_csv(f) for f in input_path.glob("*.csv")])
    # output files to csv folder
    output_file = Path(output_path) / "metadata.raw.csv"
    df.to_csv(output_file, index=False)
