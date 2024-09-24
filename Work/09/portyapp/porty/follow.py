
import os
import time
from .fileparse import parse_csv
from .stock import Stock
from .portfolio import Portfolio


def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock objects.
    '''
    filenamepath = os.path.join(os.getcwd(), filename)
    with open(filenamepath, 'rt') as lines:
        holdings_dict = parse_csv(
            lines,
            has_headers=True,
            select=['name', 'shares', 'price'],
            types=[str, int, float])
    holdings_list = [ Stock(data['name'], data['shares'], data['price']) for data in holdings_dict] 
    return holdings_list

def get_portfolio(portfolio_filename):
    holdings_list = read_portfolio(portfolio_filename)
    return Portfolio(holdings_list)


def main(args):
    print('args: ', args)
    if(len(args) != 3):
        raise SystemExit(f'Usage: {args[0]} <portfolio_filename> <stocklog_filename>')

    portfolio = get_portfolio(args[1])
    print(portfolio)
    print()

    select_stock = "CAT"
    print(f'SELECTING "{select_stock}" from the live stock feed...')
    print()

    lines = follow(args[2])
    selected_lines = filematch(lines, select_stock)
    for line in selected_lines:
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])

        if name in portfolio:
            stock = portfolio.update(name)
            stock.price = price
            print(f'Updating {name:>10s} {price:>10.2f} {change:>10.2f} >> NEW Total Value: {portfolio.total_value:.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)    
