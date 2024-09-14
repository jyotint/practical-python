# Exercise 2.16: Using the zip() function
# 'Data/missing.csv'
# 'Data/portfolio.csv'
# 'Data/portfoliodate.csv'
# 'Data/prices.csv'

import os
import sys
import csv
from pprint import pprint as pp

col_name = 'name'
col_shares = 'shares'
col_price = 'price'

def read_portfolio(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    headers = next(rows)
    portfolio = []
    for rowno, row in enumerate(rows, start=2):
        try:
            # Combine (zip) both headers and row data list
            record = dict(zip(headers, row))

            # update after the correct datatype conversion
            record[col_shares] = int(record[col_shares])
            record[col_price] = float(record[col_price])
            # print(record)

            portfolio.append(record)
        except ValueError:
            print(f"  >>> ValueError:: Bad Data >> Row #: {rowno}, Data: '{row}'")
        except Exception as ex:
            print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{ex}', Row #: {rowno}, Data: '{row}'") 

    return portfolio

def portfolio_cost(portfolio):
    total = 0.0
    for data in portfolio:
        total += data[col_shares] * data[col_price]
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
        total += data[col_shares] * new_prices[data[col_name]]
    return total

def make_report(portfolio, new_prices):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(('-' * 10 + ' ') * len(headers))
    for data in portfolio:
        name = data[col_name]
        quantity = data[col_shares]
        old_price = data[col_price]
        new_price = new_prices[name]
        change = new_price - old_price
        print(f"{name:>10s} {quantity:>10d} {old_price:>10.2f} {change:>10.2f}")


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
