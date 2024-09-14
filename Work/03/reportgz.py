# Exercise 3.15: main() functions
# Exercise 3.16: Making Scripts

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
import gzip
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


def read_portfolio_gz(filename):
    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with gzip.open(filenamepath, 'rt') as lines:
        return parse_csv(
            lines,
            has_headers=True,
            select=['name', 'shares', 'price'],
            types=[str, int, float])

def read_prices(filename):
    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath, 'rt') as lines:
        return parse_csv(
            lines, 
            has_headers=False,
            types=[str, float])

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

# def convert_str_to_required_type(colname, data):
#     converted_value = data

#     try:
#         func = selected_col_type[colname][0]    # Verbose for better clarity
#         format = selected_col_type[colname][1]
#         if len(format) == 0:
#             converted_value = func(data)
#         else:
#             converted_value = func(data, format)
#     except ValueError as ve:
#         print(f"  >>> ValueError:: Bad Data >> Data: '{data}', '{ve}'")
#         converted_value = selected_col_type[colname][2]
#     except Exception as ex:
#         print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{type(ex).__name__}', '{ex}', Data: '{data}'")
#         converted_value = selected_col_type[colname][2]

#     return converted_value

def main(args: list):
    print('args: ', args)
    if(len(args) != 3):
        raise SystemExit(f'Usage: {args[0]} <portfilename> <pricefilename>')

    portfolio_filename = args[1]
    price_filename = args[2]

    portfolio = read_portfolio_gz(portfolio_filename)
    prices = read_prices(price_filename)
    prices_dict = dict(prices)
    make_report(portfolio, prices_dict)

if __name__ == "__main__":
    main(sys.argv)
