import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

tickers_df = pd.read_csv('all.csv')
tickers = tickers_df['symbol'].tolist()

# tickers includes a list of all tickers to download data
# ex. UBER, AAPL, TSLA, MSFT etc.

# download historical daily data for all tickers to a single data frame
data = yf.download(tickers, start="2021-01-01", end="2023-04-01", group_by="ticker")

# save data to csv
data.to_csv('history.csv')
