# Exercise 2.26: The Big Picture
# 'Data/missing.csv'
# 'Data/portfolio.csv'
# 'Data/portfoliodate.csv'
# 'Data/prices.csv'
# 'Data/dowstocks.csv'

import os
import sys
import datetime
import csv
from pprint import pprint as pp


def convert_str_to_date_object(data, format):
    dateObject = datetime.date(1970, 1, 1)
    datetimeObject = datetime.datetime.strptime(data, format)
    dateObject = datetime.date(datetimeObject.year, datetimeObject.month, datetimeObject.day)
    return dateObject

csv_col_name = 'name'
csv_col_date = 'date'
csv_col_shares = 'shares'
csv_col_price = 'price'
selected_col_type = {
    csv_col_name: (str, "", "(NoName)"),
    csv_col_date: (convert_str_to_date_object, '%m/%d/%Y', datetime.date(1900, 1, 1)),
    csv_col_shares: (int, "", 0),
    csv_col_price: (float, "", 0.0)
}


def read_portfolio(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    # Get headers from file
    headers = next(rows)
    print('headers:       ', headers)

    # Locate the indices of the above columns in the source CSV file
    selected_cols = list(selected_col_type.keys())
    # print('selected_cols: ', selected_cols)
    indices = [ get_header_index(headers, colname) for colname in selected_cols ]
    # print('indices:       ', indices)

    # Construct column name and index - Changed this to list from dictionary (2_report_23-2.py).
    colname_index = list(zip(selected_cols, indices))
    print('colname_index: ', colname_index)

    portfolio = []
    for rowno, row in enumerate(rows, start=2):
        try:
            # Create record only with the required columns and not whole column set available in file
            record = { colname: convert_str_to_required_type(colname, row[index]) for colname, index in colname_index }

            portfolio.append(record)
        except ValueError as ve:
            print(f"  >>> ValueError:: Bad Data >> Row #: {rowno}, Data: '{row}', '{ve}'")
        except Exception as ex:
            print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{type(ex).__name__}', '{ex}', Row #: {rowno}, Data: '{row}'") 

    return portfolio

def get_header_index(headers, colname):
    return headers.index(colname)

def convert_str_to_required_type(colname, data):
    converted_value = data

    try:
        func = selected_col_type[colname][0]    # Verbose for better clarity
        format = selected_col_type[colname][1]
        if len(format) == 0:
            converted_value = func(data)
        else:
            converted_value = func(data, format)
    except ValueError as ve:
        print(f"  >>> ValueError:: Bad Data >> Data: '{data}', '{ve}'")
        converted_value = selected_col_type[colname][2]
    except Exception as ex:
        print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{type(ex).__name__}', '{ex}', Data: '{data}'")
        converted_value = selected_col_type[colname][2]

    return converted_value

def portfolio_cost(portfolio):
    total = 0.0
    for data in portfolio:
        total += data[csv_col_shares] * data[csv_col_price]
    return total

def read_prices(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    # No header in this prices.csv, so skipping it
    # headers = next(rows)

    prices = {}
    for rowno, row in enumerate(rows, start=1):
        try:
            name = row[0]
            quantity = float(row[1])

            prices[name] = quantity
            # print("Row Added: ", name, quantity)
        except ValueError:
            print(f"  >>> ValueError:: Bad Data >> Row #: {rowno}, Data: '{row}'")
        except Exception as ex:
            print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{ex}', Row #: {rowno}, Data: '{row}'") 

    # pp(prices)
    return prices

def calculate_gain_loss(portfolio, new_prices):
    total = 0.0
    for data in portfolio:
        total += data[csv_col_shares] * new_prices[data[csv_col_name]]
    return total

def make_report(portfolio, new_prices):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(('-' * 10 + ' ') * len(headers))
    for data in portfolio:
        name = data[csv_col_name]
        quantity = data[csv_col_shares]
        old_price = data[csv_col_price]
        new_price = new_prices[name]
        change = new_price - old_price
        print(f"{name:>10s} {quantity:>10d} {old_price:>10.2f} {change:>10.2f}")


print('Reading Portfolio...')
# portfolioFilename = 'missing.csv'
# portfolioFilename = 'portfolio.csv'
portfolioFilename = 'portfoliodate.csv'
# portfolioFilename = 'dowstocks.csv'
print(f'Reading portfolio from "{portfolioFilename}"...')
portfolio = read_portfolio(portfolioFilename)

print('Calculating Portfolio value...')
old_value = portfolio_cost(portfolio)
print(f'Current Portfolio Value: {old_value}')
print('')

pricesFilename = 'prices.csv'
print(f'Reading current stock prices from "{pricesFilename}"...')
prices = read_prices(pricesFilename)

print('')
print('Calculating the NEW Portfolio value...')
new_value = calculate_gain_loss(portfolio, prices)
print(f'    NEW Portfolio Value: {new_value}')

print('')
gl = new_value - old_value
print(f'            Gain / Loss: {gl:<15.2f}')

print('')
make_report(portfolio, prices)
