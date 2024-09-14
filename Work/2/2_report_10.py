# Exercise 2.9: Collecting Data
# 'Data/portfolio.csv'
# 'Data/prices.csv'

import os
import sys
import csv
from pprint import pprint as pp


def read_portfolio(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    headers = next(rows)
    portfolio = []
    for row in rows:
        try:
            name = row[0]
            quantity = int(row[1])
            unit_cost = float(row[2])
            data = {
                'name': row[0], 
                'quantity': quantity, 
                'unit_cost': unit_cost
            }
            portfolio.append(data)
        except ValueError:
            print('  >>> Invalid row', row)
        except Exception as ex:
            print(f"  >>> Catch ALL Exceptions >> Type: '{ex}', Invalid Row: '{row}'") 

    return portfolio

def portfolio_cost(portfolio):
    total = 0.0
    for data in portfolio:
        total += data['quantity'] * data['unit_cost']
    return total

def read_prices(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    # No header in this prices.csv, so skipping it
    # headers = next(rows)

    prices = {}
    for row in rows:
        try:
            name = row[0]
            quantity = float(row[1])

            prices[name] = quantity
            # print("Row Added: ", name, quantity)
        except ValueError:
            print('  >>> ValueError: Invalid row', row)
        except Exception as ex:
            print(f"  >>> Catch ALL Exceptions >> Type: '{ex}', Invalid Row: '{row}'") 

    pp(prices)
    return prices

def calculate_gain_loss(portfolio, new_prices):
    total = 0.0
    for data in portfolio:
        total += data['quantity'] * new_prices[data['name']]
    return total

def make_report(portfolio, new_prices):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(('-' * 10 + ' ') * len(headers))
    for data in portfolio:
        name = data['name']
        quantity = data['quantity']
        old_price = data['unit_cost']
        new_price = new_prices[name]
        change = new_price - old_price
        print(f"{name:>10s} {quantity:>10d} {old_price:>10.2f} {change:>10.2f}")


portfolioFilename = 'portfolio.csv'
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
print(f'            Gain / Loss: {new_value - old_value}')

print('')
make_report(portfolio, prices)
