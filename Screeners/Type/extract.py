# read merged.csv file and extract several columns and rename them
# Symbol -> symbol
# Name -> name
# asset_type -> asset_type

import pandas as pd

# first row of the csv file is the header

df = pd.read_csv('merged.csv')

# extract several columns and rename them
df = df[['Symbol', 'Name', 'asset_type']]
df.columns = ['symbol', 'name', 'asset_type']

# save the extracted dataframe to a csv file
df.to_csv('extracted.csv', index=False)
