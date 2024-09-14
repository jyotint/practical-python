# Exercise 3.3: Reading CSV Files
# 'Data/portfolio.csv'

import os
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into the list of records
    '''

    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath) as f:
        rows = csv.reader(f)

        # Read file header
        headers = next(rows)
        records = []

        for row in rows:
            if not row:     # Skip row with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records

portfolio_filename = 'portfolio.csv'
print(f'Reading portfolio from "{portfolio_filename}"...')
portfolio = parse_csv(portfolio_filename)
