import os
import logging
from .stock import Stock
from . import fileparse
from .portfolio import Portfolio
from .tableformatter import TableFormatter
from .tableformatterexception import TableFormatterException
from .texttableformatter import TextTableFormatter
from .csvtableformatter import CSVTableFormatter


log = logging.getLogger(__name__)

def get_portfolio(filepath):
    log.info(f'Reading PORTFOLIO from "{filepath}" file...')
    filenamepath = os.path.join(os.getcwd(), filepath)
    with open(filenamepath, 'rt') as lines:
        portfolio = Portfolio.read_csv(lines)
    log.info(f'  DONE ({str(portfolio)})')
    return portfolio

def read_prices_file(filepath):
    '''
    Read a CSV file of price data into a dict of Price objects.
    '''
    log.info(f'Reading PRICES from "{filepath}" file...')
    filenamepath = os.path.join(os.getcwd(), filepath)
    with open(filenamepath, 'rt') as lines:
        price_tuples, errored_records = fileparse.parse_csv(
            lines, 
            has_headers=False,
            types=[str, float])

    log.info(f'  DONE (count: {len(price_tuples)})')
    return price_tuples

def make_report_data(portfolio: list[Stock], new_prices: list[tuple]) -> list:
    '''
    Make a list of (name, shares, old_price, new_price, change) tuples 
    given a portfolio list and prices dictionary.
    '''
    log.info('Building report data...')
    report_data = []
    new_prices_dict = dict(new_prices)
    for data in portfolio:
        name = data.name
        quantity = data.shares
        old_price = data.price
        new_price = new_prices_dict[name]
        change = new_price - old_price
        report_data.append((name, quantity, old_price, new_price, change))

    log.info(f'  DONE (count: {len(report_data)}).')
    return report_data

def print_report(report_data, formatter: str | TableFormatter = 'Text'):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''

    log.info('Printing report data...')
    if isinstance(formatter, str):
        formatter = _create_formatter(formatter)

    headers = ('Name','Shares','OldPrice','NewPrice','Change')
    formatter.headings(headers)
    for row in report_data:
        formatter.row(row)

def print_table(list_data, formatter: str | TableFormatter = 'text', columns: list = None):
    '''
    Print a nicely formatted table. If a row in the 'list_data' is of type
        'tuple' or 'list', then all columns data will be printed
        'dict' or 'object', then supplied 'columns' filter will be applied
    '''

    log.info('Printing table data...')
    if isinstance(formatter, str):
        formatter = _create_formatter(formatter)

    formatter.headings(columns)
    row = list_data[0]
    print(f'Type: "{type(row)}",  IsList: {isinstance(row, list)},  IsTuple: {isinstance(row, tuple)},  IsDict: {isinstance(row, dict)},  IsObject: {isinstance(row, object)}')
    for row in list_data:
        if isinstance(row, tuple):
            row = list(row)
        if isinstance(row, list):
            row = list(row)
        elif isinstance(row, dict):
            row = [ row[colname] for colname in columns ] 
        elif isinstance(row, object):
            row = [ getattr(row, colname) for colname in columns ] 
        else:
            row = list(row)
        formatter.row(row)

def _create_formatter(fmt):
    match fmt:
        case TextTableFormatter.formatter_name:
            return TextTableFormatter()
        case CSVTableFormatter.formatter_name:
            return CSVTableFormatter()
        case _:
            raise TableFormatterException(fmt)
