# Exercise 3.12: Using your library module (Original file: '2_report_26.py')
# Take that program and modify it so that all of the input file processing is done using functions in your fileparse module. 
# To do that, import fileparse as a module and change the read_portfolio() and read_prices() functions to use the parse_csv() function.

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
from fileparse import parse_csv


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
    return parse_csv(
        filename=filename,
        has_headers=True,
        select=['name', 'shares', 'price'],
        types=[str, int, float])

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
    return parse_csv(
        filename=filename, 
        has_headers=False,
        types=[str, float])

def calculate_gain_loss(portfolio: list, new_prices_dict: dict):
    total = 0.0
    for data in portfolio:
        total += data[csv_col_shares] * new_prices_dict[data[csv_col_name]]
    return total

def make_report(portfolio: list, new_prices_dict: dict):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(('-' * 10 + ' ') * len(headers))
    for data in portfolio:
        name = data[csv_col_name]
        quantity = data[csv_col_shares]
        old_price = data[csv_col_price]
        new_price = new_prices_dict[name]
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
prices_dict = dict(prices)

print('')
print('Calculating the NEW Portfolio value...')
new_value = calculate_gain_loss(portfolio, prices_dict)
print(f'    NEW Portfolio Value: {new_value}')

print('')
gl = new_value - old_value
print(f'              Gain/Loss: {gl:<15.2f}')

print('')
make_report(portfolio, prices_dict)
