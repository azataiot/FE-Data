# Financial Sectors

Sorted according to the [GICS](https://en.wikipedia.org/wiki/GICS) classification.

```python
import pandas as pd

# Create a list of dictionaries containing sector codes and names
sector_list = [
    {"Code": "10", "Name": "Energy"},
    {"Code": "15", "Name": "Materials"},
    {"Code": "20", "Name": "Industrials"},
    {"Code": "25", "Name": "Consumer Discretionary"},
    {"Code": "30", "Name": "Consumer Staples"},
    {"Code": "35", "Name": "Health Care"},
    {"Code": "40", "Name": "Financials"},
    {"Code": "45", "Name": "Information Technology"},
    {"Code": "50", "Name": "Communication Services"},
    {"Code": "55", "Name": "Utilities"},
    {"Code": "60", "Name": "Real Estate"}
]

# Create the pandas dataframe from the sector list
sectors = pd.DataFrame(sector_list)

# Print the dataframe
print(sectors)

```

