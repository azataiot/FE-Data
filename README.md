# Financial Engineering Data(FED)

This repository includes more than **1000** financial assets historical price and metadata starting from ~~**2021-01-01**~~ (earliest supported date) to **~~2023-04-01~~** (latest supported date).

Extra data can be downloaded and added with the python scripts provided in this repository.

This repo also includes markets, sectors and other categorial informations with usefull scripts written in Python and R.

Notice: Minimum Python version required: `3.10.2` , and Minimum R version required: `4.1.3`

## Contents

### Asset MetaData DB

- `metadata.raw.csv` [sample](./data/metadata.raw.csv)
  - Raw data includes only `symbol`, and `name` columns.
- `metadata.profile.csv`
  - Includes everything in `metadata.raw.csv` 
  - Includes other profiling meta data about the asset, click [here]() for a sample.
- `metadata.csv`
  - Includes everything in `metadata.profile.csv`
  - Includes `start_date` columns for earliest awailable data.
- `metadata.min.csv`
  - Derived from `metadata.csv` but keep only crusial columns such as:
    - `symbol`
    - `name`
    - `market`
    - `sector*`
    - `industry*`
    - `country*`
    - `start_date`



### Asset Price DB (OHLC)





### Financial Markets Classification

There is a problem in the financial world, different platforms and different companies uses different standards to describe same security or asset type, or same companies some times have several different equities on different markets with same or similar names. 

To solve this problem I decided to review different types of data platforms and setup a unified way to describe data. 

#### FED Financial Markets

![FED](./assets/README.assets/Markets.svg)

If you interested on how other platforms classified financial market, click [financial markets](./docs/financial markets.md).

### Financial Sectors Classification

#### FED Financial Sectors

![FED Sectors](./assets/README.assets/Sectors.svg)



