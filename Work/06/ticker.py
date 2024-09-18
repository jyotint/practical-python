# Exercise 6.10: Making more pipeline components
# Exercise 6.11: Filtering data
# ticker.py

from rt_follow0608 import follow, get_portfolio
from portfolio import Portfolio
import csv


def select_columns(rows: list[str], indices: list[int]):
    print(f'  select_columns():: indices: "{indices}"')
    print(f'  select_columns():: rows:    "{rows}"')
    for row in rows:
        print(f'  select_columns():: Inside loop: "{row[0]}"')
        yield [ row[index] for index in indices ]

def convert_types(rows: list[str], types: list[type]):
    print(f'  convert_types():: types: "{types}"')
    print(f'  convert_types():: rows:  "{rows}"')
    for row in rows:
        print(f'  convert_types()::  Inside loop: "{row[0]}"')
        yield [ func(value) for func, value in zip(types, row) ]

def make_dict(rows: list, headers: list[str]):
    print(f'  make_dict():: headers: "{headers}"')
    print(f'  make_dict():: rows:    "{rows}"')
    for row in rows:
        print(f'  make_dict()::      Inside loop: "{row[0]}"')
        yield dict(zip(headers, row))

# Exercise 6.15: Code simplification
# def filter_data(rows: dict, names: list[str]):
#     print(f'  filter_data():: names: "{names}"')
#     print(f'  filter_data():: rows:  "{rows}"')
#     for row in rows:
#         print(f'  filter_data()::    Inside loop: "{row['name']}"')
#         if row['name'] in names:
#             yield row
def filter_data(rows: dict, names: list[str]):
    return (row for row in rows if row['name'] in names)

def parse_stock_data(lines: list):
    rows = csv.reader(lines)
    print('parse_stock_data()::Calling select_columns()...')
    rows = select_columns(rows, [0, 1, 4])
    print('parse_stock_data()::Calling convert_types()...')
    rows = convert_types(rows, [str, float, float])
    print('parse_stock_data()::Calling make_dict()...')
    rows = make_dict(rows, ['name', 'price', 'change'])
    print('parse_stock_data()::Returning.')
    return rows

if __name__ == "__main__":
    print('main()::Calling get_portfolio()...')
    portfolio = get_portfolio('Data/portfolio.csv')
    print()

    print('main()::Calling follow()...')
    lines = follow('Data/stocklog.csv')
    print('main()::Calling parse_stock_data()...')
    rows = parse_stock_data(lines)
    print('main()::Calling filter_data()...')
    names = [ stock.name for stock in portfolio.holdings ]
    rows = filter_data(rows, names)
    print('main()::Starting loop...')
    for row in rows:
        print('main()::Inside loop...')
        print(row)
