# Financial Engineering Data(FED)

<p align="center">
  <a href="https://github.com/azataiot/FE-Data"><img src="assets/img/logo.png" alt="Financial Engineering Data"></a>
</p>
<p align="center">
    <em>Financial engineering data for Education and Research, aiming sustainability and efficency</em>
</p>


---

We aim to prive a centralized repository for financial engineering data, hepling to **reduce the burden on the data providers** like Yahoo Finance and making it more efficient for developers to access and use financial data.

This repository includes financial assets historical price and metadata starting from ~~**2021-01-01**~~ (earliest supported date) to **~~2023-04-01~~** (latest supported date).

Extra data can be downloaded and added with ~~the python scripts provided~~ (automation) in this repository.

This repo also includes markets, sectors and other categorial informations with usefull scripts written in Python and R.

Notice: Minimum Python version required: `3.10.2` , and Minimum R version required: `4.1.3`

## LEGAL DISCLAIMER

ANY CONTENT YOU’VE ACCESSED FROM THIS REPOSITORY OR USING THE CODE PROVIDED BY THIS REPOSITORY IS EDUCATIONAL AND ACADEMIC PURPOSE ONLY. THIS REPO IS NOT AFFILIATED OR ENDORSED IN ANY TERMS WITH YAHOO, INC.

**You should refer to Yahoo!'s terms of use** ([here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm), [here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and [here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) **for details on your rights to use the actual data downloaded.**

## Contents

### Asset MetaData DB

- `metadata.raw.csv` [sample](./data/metadata.raw.csv)
  - Raw data includes only `symbol`, and `name` columns.
- `metadata.profile.csv`
  - Includes everything in `metadata.raw.csv` 
  - Includes other profiling meta data about the asset, click [here]() for a sample.
- `metadata.extra.csv`
  - Includes everything in `metadata.profile.csv`
  - Includes `start_date` columns for earliest awailable data.
- `metadata.csv`
  - Derived from `metadata.extra.csv` but keep only crusial columns such as:
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

## License (s)

CODE in this repo is licensed under MIT license.

DATA in this repo: check Yahoo!'s terms of use** ([here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm), [here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html), and [here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) **for details on your rights to use the actual data downloaded.**

THIRDPARTY:  thirdparty libraries or tools in this repo and their licenses are located in the[ licenses folder](./licenses).
