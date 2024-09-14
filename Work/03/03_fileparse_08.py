# Exercise 3.8: Raising exceptions
# 'Data/portfolio.csv'
# 'Data/portfoliodate.csv'
# 'Data/portfolio.csv'

import os
import csv
import datetime


def convert_str_to_date_object(data):
    dateObject = datetime.date(1970, 1, 1)
    datetimeObject = datetime.datetime.strptime(data, '%m/%d/%Y')
    dateObject = datetime.date(datetimeObject.year, datetimeObject.month, datetimeObject.day)
    return dateObject

def convert_str_to_time_object(data):
    dateObject = datetime.date(1970, 1, 1)
    datetimeObject = datetime.datetime.strptime(data, '%I:%M%p')
    dateObject = datetime.time(datetimeObject.hour, datetimeObject.minute, datetimeObject.second)
    return dateObject


def parse_csv(
        filename: str, 
        file_data_delimiter: str = ",",
        file_has_header: bool = True,
        select: list = None, 
        types: list = None) -> list:
    '''
    Parse a CSV file into the list of records.
    '''

    # print('Parameter: filename:', filename)
    # print('Parameter: select:', select)
    # print('Parameter: types:', types)

    if select and file_has_header == False:
        raise RuntimeError("'select' argument requires column headers!")

    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath) as f:
        rows = csv.reader(f, delimiter=file_data_delimiter)

        selected_indices = []
        if file_has_header == True:
            # Read file header
            selected_headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                selected_indices = [ selected_headers.index(colname) for colname in select ]
                selected_headers = select

        records = []
        for row in rows:
            if not row:     # Skip row with no data
                continue

            if selected_indices:
                row = [ row[index] for index in selected_indices ]

            if types:
                row = [ func(data) for func, data in zip(types, row)]

            if file_has_header == True:
                # print('row (converted): ', row)
                record = dict(zip(selected_headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


# portfolio_filename = 'portfolio.csv'
portfolio_filename = 'portfoliodate.csv'
print(f'Reading portfolio (1) from "{portfolio_filename}"...')
portfolio1 = parse_csv(portfolio_filename)

print(f'Reading portfolio (2) from "{portfolio_filename}"...')
portfolio2 = parse_csv(
    portfolio_filename, 
    select=['name', 'shares', 'price'])

print(f'Reading portfolio (3) from "{portfolio_filename}"...')
portfolio3 = parse_csv(
    portfolio_filename,
    types=[str, convert_str_to_date_object, convert_str_to_time_object, int, float])

print(f'Reading portfolio (4) from "{portfolio_filename}"...')
portfolio4 = parse_csv(
    portfolio_filename, 
    select=['name', 'shares', 'price'],
    types=[str, int, float])

portfolio_filename = 'portfolio.dat'
print(f'Reading portfolio (5) from "{portfolio_filename}"...')
portfolio5 = parse_csv(
    portfolio_filename, 
    file_has_header=True,
    file_data_delimiter=" ",
    select=['name', 'shares', 'price'],
    types=[str, int, float])


prices_filename = 'prices.csv'
print(f'Reading prices (1) from "{prices_filename}"...')
prices1 = parse_csv(
    prices_filename, 
    file_has_header=False)

print(f'Reading prices (2) from "{prices_filename}"...')
prices2 = parse_csv(
    prices_filename, 
    file_has_header=False,
    types=[str, float])

portfolio_filename = 'portfoliodate.csv'
print(f'Reading portfolio (6) from "{portfolio_filename}" (Throwing Exception example for bad parameters)...')
portfolio6 = parse_csv(
    portfolio_filename, 
    file_has_header=False,
    select=['name', 'shares', 'price'],
    types=[str, int, float])
