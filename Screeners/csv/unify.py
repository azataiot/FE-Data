import pandas as pd
import os

# get all csv files in this directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
print(files)

dfs = []
for f in files:
    df = pd.read_csv(f)
    dfs.append(df)

# merge all dataframes into one single dataframe
df = pd.concat(dfs, ignore_index=True)

# remove duplicates
df.drop_duplicates(inplace=True)

# remove rows with empty symbol
df.dropna(subset=['Symbol'], inplace=True)

# extract several columns and rename them
df = df[['Symbol', 'Name']]
df.columns = ['symbol', 'name']

# save the extracted dataframe to a csv file
df.to_csv('all.csv', index=False)
