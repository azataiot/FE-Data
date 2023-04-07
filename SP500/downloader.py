import pandas as pd
import yfinance as yf
import requests
from datetime import datetime, timedelta

# Download S&P 500 component stocks from Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
html = requests.get(url).content
df_list = pd.read_html(html)
sp500_df = df_list[0]

# Keep only the columns we need
sp500_df = sp500_df[['Symbol', 'Security', 'GICS Sector', 'GICS Sub-Industry', 'Headquarters Location', 'Founded', 'CIK']]

# Rename columns for clarity
sp500_df.columns = ['symbol', 'security', 'sector', 'sub_industry', 'headquarters', 'founded', 'cik']

# Set the symbol as the DataFrame index
sp500_df.set_index('symbol', inplace=True)

# Set the start and end dates for the historical data
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 4, 1)

# Download historical daily quote data from Yahoo Finance for each stock
dfs = []
for symbol in sp500_df.index:
    stock = yf.Ticker(symbol)
    df = stock.history(start=start_date, end=end_date)
    df['symbol'] = symbol
    dfs.append(df)

# Merge the historical data with the S&P 500 component stocks DataFrame
sp500_hist_df = pd.concat(dfs, axis=0, ignore_index=False)
sp500_hist_df = pd.merge(sp500_hist_df, sp500_df, on='symbol')

# Display the combined DataFrame
print(sp500_hist_df.head())
