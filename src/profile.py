import json
import multiprocessing as mp
from pathlib import Path
from yahoofinancials import YahooFinancials
from yahoofinancials.etl import ManagedException
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
