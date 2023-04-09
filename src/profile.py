import json
import multiprocessing as mp
from pathlib import Path

import pandas as pd
from yahoofinancials import YahooFinancials
from yahoofinancials.etl import ManagedException

from .const import profile_csv_columns, raw_csv_columns, extra_csv_columns
from .models import Profile
from .utility import create_folder


# define a function to download and save the profile data for a single ticker
def download_profile(symbol: str) -> dict:
    yf = YahooFinancials(symbol)
    # try catch block to handle the error when the ticker is not found
    # try to wait for 1 minute  to complete the download, if not complete, return an empty dictionary
    try:
        print(f"Downloading profile for {symbol}...")
        profile = yf.get_stock_profile_data()[symbol]
    except ManagedException:
        print(f"Failed to download profile for {symbol}")
        profile = {}
    return profile


def save_profile(symbol: str, output_dir: Path | str) -> None:
    # create the output folder if it does not exist
    create_folder(output_dir)
    # check if the file exists
    if (output_dir / f"{symbol}.json").is_file():
        print(f"Profile for {symbol} already exists. Skipping...")
        return
    profile = download_profile(symbol)
    with open(output_dir / f"{symbol}.json", "w") as f:
        json.dump(profile, f)
        print(f"Profile for {symbol} saved to {output_dir / f'{symbol}.json'}")


# define a function to download and save all the profile to separate json files
def download_all_profiles(symbols: list[str], output_dir: Path | str) -> None:
    with mp.Pool(processes=mp.cpu_count()) as pool:
        pool.starmap(save_profile, [(ticker, output_dir) for ticker in symbols])


# define a function to read the profile data from the json file and return the Profile object
def read_profile(symbol: str, input_dir: Path | str) -> Profile:
    with open(input_dir / f"{symbol}.json") as f:
        profile = Profile(**json.load(f))
    return profile


# define a function to populate profile.csv from metadata.raw.csv and profile json files
def populate_profile_csv(metadata_dir: Path | str, json_files_dir: Path | str, output_dir: Path | str) -> None:
    # create the output folder if it does not exist
    create_folder(output_dir)
    # read the metadata.raw.csv file
    with open(metadata_dir / "metadata.raw.csv") as f:
        df = pd.read_csv(f)
    # create new columns in the dataframe
    df.reindex(columns=profile_csv_columns)
    # iterate over the dataframe and populate the new columns
    for index, row in df.iterrows():
        symbol = row["symbol"]
        profile = read_profile(symbol, json_files_dir)
        for column in profile_csv_columns:
            if column in raw_csv_columns:
                continue
            df.loc[index, column] = getattr(profile, column)
    # save the dataframe to csv file
    with open(output_dir / "metadata.profile.csv", "w") as f:
        f.write(df.to_csv(index=False))


def read_ohlcv(symbol: str, input_dir: Path | str) -> pd.DataFrame:
    with open(input_dir / f"{symbol}.csv") as f:
        ohlcv = pd.read_csv(f)
    return ohlcv


def populate_extra_csv(profile_dir: Path | str, ohlcv_files_dir: Path | str, output_dir: Path | str) -> None:
    # create the output folder if it does not exist
    create_folder(output_dir)
    # read the metadata.raw.csv file
    with open(profile_dir / "metadata.profile.csv") as f:
        df = pd.read_csv(f)
    # create new columns in the dataframe
    df.reindex(columns=extra_csv_columns)
    # iterate over the dataframe and populate the new columns
    for index, row in df.iterrows():
        symbol = row["symbol"]
        ohlcv = read_ohlcv(symbol, ohlcv_files_dir)
        df.loc[index, "start_date"] = ohlcv["Date"].min()
    # save the dataframe to csv file
    with open(output_dir / "metadata.extra.csv", "w") as f:
        f.write(df.to_csv(index=False))
