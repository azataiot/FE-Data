# looping through all of them one by one is too slow, so we'll use multiprocessing
# to speed things up
import json
from pathlib import Path
from multiprocessing import Pool

import pandas as pd
from yahoofinancials import YahooFinancials

tickers_df = pd.read_csv('all.csv')
tickers = tickers_df['symbol'].tolist()

# get a list of json profile files saved in the profiles folder, using pathlib
profiles = [str(p) for p in Path('profiles').glob('*.json')]
# filter out tickers that already have a profile json file
tickers = [t for t in tickers if 'profiles/' + t + '.json' not in profiles]


# define a function to download and save the profile data for a single ticker
def download_profile(ticker):
    print(f"processing {ticker}...")
    yf = YahooFinancials(ticker)
    profile_json = yf.get_stock_profile_data()[ticker]
    # save json files to profiles folder
    with open('profiles/' + ticker + '.json', 'w') as f:
        json.dump(profile_json, f)
    print(f"saved {ticker} profile data to profiles/{ticker}.json")


# use multiprocessing to download and save the profile data for all tickers
if __name__ == '__main__':
    with Pool() as pool:
        pool.map(download_profile, tickers)
