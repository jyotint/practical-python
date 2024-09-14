# Exercise 3.4: Building a Column Selector
# 'Data/portfolio.csv'
# 'Data/portfoliodate.csv'

import os
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into the list of records
    '''

    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath) as f:
        rows = csv.reader(f)

        # Read file header
        selected_headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [ selected_headers.index(colname) for colname in select ]
            selected_headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:     # Skip row with no data
                continue
            if indices:
                row = [ row[index] for index in indices ]

            record = dict(zip(selected_headers, row))
            records.append(record)

    return records

# portfolio_filename = 'portfolio.csv'
portfolio_filename = 'portfoliodate.csv'
print(f'Reading portfolio from "{portfolio_filename}"...')
portfolio1 = parse_csv(portfolio_filename)
portfolio2 = parse_csv(portfolio_filename, select=['name', 'shares', 'price'])
