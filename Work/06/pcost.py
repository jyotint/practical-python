# Exercise 6.2: Supporting Iteration
# pcost.py

import os
import fileparse
from stock import Stock
from portfolio import Portfolio


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock objects.
    '''
    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath, 'rt') as lines:
        holdings_dict = fileparse.parse_csv(
            lines,
            has_headers=True,
            select=['name', 'shares', 'price'],
            types=[str, int, float])
    holdings_list = [ Stock(data['name'], data['shares'], data['price']) for data in holdings_dict] 
    return holdings_list

def portfolio_cost(portfolio_filename):
    print(f'Reading portfolio (1) from "{portfolio_filename}"...')
    holdings_list = read_portfolio(portfolio_filename)
    portfolio = Portfolio(holdings_list)
    print(f'Total Cost: {portfolio.total_value:.2f}')

def main(args):
    print('args: ', args)
    if(len(args) != 2):
        raise SystemExit(f'Usage: {args[0]} <portfilename>')
    portfolio_cost(args[1])

if __name__ == "__main__":
    import sys
    main(sys.argv)
