# Exercise 6.7: Watching your portfolio
# Run the Producer in separate terminal "winpty py stocksim.py"

# rt_follow3.up

import os
import time
import fileparse
from stock import Stock
from portfolio import Portfolio


def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock objects.
    '''
    filenamepath = os.path.join(os.getcwd(), filename)
    with open(filenamepath, 'rt') as lines:
        holdings_dict = fileparse.parse_csv(
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

    for line in follow(args[2]):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])

        if name in portfolio:
            stock = portfolio.find(name)
            stock.price = price
            print(f'Updating {name:>10s} {price:>10.2f} {change:>10.2f} >> NEW Total Value: {portfolio.total_value:.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)    
