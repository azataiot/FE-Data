import json
from pathlib import Path

import pandas as pd
from yahoofinancials import YahooFinancials

tickers_df = pd.read_csv('all.csv')
tickers = tickers_df['symbol'].tolist()

# get a list of json profile files saved in the profiles folder, using pathlib
profiles = [str(p) for p in Path('profiles').glob('*.json')]

for each in tickers:
    print(f"processing {each}...")
    # if the json file for the ticker is already saved, skip it
    if 'profiles/' + each + '.json' in profiles:
        print(f"already exists, skipping {each}...")
        continue
    yf = YahooFinancials(each)
    profile_json = yf.get_stock_profile_data()[each]
    # save json files to profiles folder
    with open('profiles/' + each + '.json', 'w') as f:
        json.dump(profile_json, f)
    print(f"saved {each} profile data to profiles/{each}.json")



