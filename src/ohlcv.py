from datetime import datetime
from pathlib import Path
import yfinance as yf
import pandas as pd
import multiprocessing as mp
from .utility import create_folder, file_exists
from .exceptions import SymbolOHLVCExistsException, EmptyResponseException


def download_ohlcv(symbol, output_dir):
    # create the folder if not exists
    create_folder(output_dir)
    ticker = yf.Ticker(symbol)
    data = ticker.history("10y", interval="1d", start="1900-01-01")
    # save the data
    data.to_csv(output_dir / f"{symbol}.csv")


def add_symbol_ohlcv(symbol, output_dir) -> bool:
    print(f"Adding {symbol}...")
    # create the folder if not exists
    create_folder(output_dir)
    symbol_file = output_dir / f"{symbol}.csv"
    if file_exists(symbol_file):
        print(f"Symbol {symbol} already exists. Skipping...")
        return False
    ticker = yf.Ticker(symbol)
    data = ticker.history("10y")
    if data.empty:
        print(f"Empty response for {symbol}. Skipping...")
        return False
    # save the data
    data.to_csv(symbol_file)
    return True


def add_symbol_ohlcv_batch(symbols, output_dir):
    with mp.Pool(processes=mp.cpu_count()) as pool:
        # handle exceptions
        pool.starmap(add_symbol_ohlcv, [(symbol, output_dir) for symbol in symbols])


# Define function to download historical data for all tickers in parallel
def download_all_ohlcv(symbols, to_dir):
    with mp.Pool(processes=mp.cpu_count()) as pool:
        pool.starmap(download_ohlcv, [(symbol, to_dir) for symbol in symbols])


# download_ohlcv("AAPL", Path("data/ohlcv"))
def check_dw():
    print(Path.cwd())
    ticker = yf.Ticker("MSFT")
    data = ticker.history("max")
    print(data.empty)
    print(data)


if __name__ == "__main__":
    check_dw()
