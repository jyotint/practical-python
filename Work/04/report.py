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
from fileparse import parse_csv
from stock import Stock
from tableformatter import TableFormatter
from tableformatterexception import TableFormatterException
from texttableformatter import TextTableFormatter
from csvtableformatter import CSVTableFormatter

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock objects.
    '''
    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath, 'rt') as lines:
        portfolio_dict = parse_csv(
            lines,
            has_headers=True,
            select=['name', 'shares', 'price'],
            types=[str, int, float])
    portfolio = [ Stock(data['name'], data['shares'], data['price']) for data in portfolio_dict] 
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict of Price objects.
    '''
    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath, 'rt') as lines:
        price_tuples = parse_csv(
            lines, 
            has_headers=False,
            types=[str, float])
    return price_tuples

def make_report_data(portfolio: list[Stock], new_prices: list):
    '''
    Make a list of (name, shares, old_price, new_price, change) tuples 
    given a portfolio list and prices dictionary.
    '''
    report_data = []
    for data in portfolio:
        name = data.name
        quantity = data.shares
        old_price = data.price
        new_price = new_prices[name]
        change = new_price - old_price
        report_data.append((name, quantity, old_price, new_price, change))
    return report_data

def create_formatter(fmt):
    match fmt:
        case TextTableFormatter.formatter_name:
            return TextTableFormatter()
        case CSVTableFormatter.formatter_name:
            return CSVTableFormatter()
        case _:
            raise TableFormatterException(fmt)

def print_report(report_data, formatter: TableFormatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','OldPrice','NewPrice','Change')
    #02 print('%10s %10s %10s %10s %10s' % headers)
    #02 print(('-'*10 + ' ')*len(headers))
    formatter.headings(headers)
    for row in report_data:
        #02 print('%10s %10d %10.2f %10.2f %10.2f' % row)
        formatter.row(row)

def print_table(list_data, columns: list, formatter: TableFormatter):
    '''
    Exercise 4.10: An example of using getattr()
    Print a nicely formated table.
    '''
    formatter.headings(columns)
    for element in list_data:
        row = [ getattr(element, colname) for colname in columns] 
        formatter.row(row)

def portfolio_report(portfolio_filename, price_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    print(f'Reading portfolio (1) from "{portfolio_filename}"...')
    portfolio_1 = read_portfolio(portfolio_filename)

    print(f'Reading prices (1) from "{price_filename}"...')
    prices_1 = read_prices(price_filename)
    prices = dict(prices_1)

    report_data = make_report_data(portfolio_1, prices)
    formatter = create_formatter(fmt)
    print_report(report_data, formatter)

def main(args: list):
    print('args: ', args)
    if(len(args) != 4):
        raise SystemExit(f'Usage: {args[0]} <portfilename> <pricefilename> <formatter>')

    portfolio_report(args[1], args[2], args[3])

if __name__ == "__main__":
    main(sys.argv)
