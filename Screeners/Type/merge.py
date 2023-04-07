# read all csv files from this directory and merge them into one single pandas dataframe with Columns as 'symbol' ,
# 'name' , 'asset_type'

import pandas as pd
import os

# get all csv files in this directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
print(files)

# read all csv files into a list of pandas dataframes,each dataframe should add another column named 'asset_type',
# which is the name of the csv file

dfs = []
for f in files:
    df = pd.read_csv(f)
    df['asset_type'] = f.replace('.csv', '')
    dfs.append(df)

# merge all dataframes into one single dataframe
df = pd.concat(dfs, ignore_index=True)

# remove duplicates
df.drop_duplicates(inplace=True)

# save the merged dataframe to a csv file
df.to_csv('merged.csv', index=False)

