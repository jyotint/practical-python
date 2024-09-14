# Exercise 2.24: First-class Data
# 'Data/missing.csv'
# 'Data/portfolio.csv'
# 'Data/portfoliodate.csv'
# 'Data/prices.csv'

import os
import sys
import csv
from pprint import pprint as pp

csv_col_name = 'name'
csv_col_shares = 'shares'
csv_col_price = 'price'
selected_col_type = {
    csv_col_name: str,
    csv_col_shares: int,
    csv_col_price: float
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
    func = selected_col_type[colname]   # Verbose for better clarity
    return func(data)

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
