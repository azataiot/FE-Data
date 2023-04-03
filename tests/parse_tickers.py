# tests / parse_tickers.py
# Created by azat at 3.04.2023


import csv

# Open the CSV file
with open('/Volumes/Data 1/Developer/FE-Project/tests/quotes-crypto.csv', 'r') as f:
    # Create a CSV reader object
    reader = csv.reader(f)
    # Use next() to skip the header row
    next(reader)
    # Initialize an empty list to store the contents of the first column
    first_column_contents = []
    # Loop over each row in the CSV file
    for row in reader:
        # Append the contents of the first column to the list
        first_column_contents.append(row[0])

# Print the list of contents of the first column
print(first_column_contents)
