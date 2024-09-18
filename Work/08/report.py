# Exercise 7.11: Class Methods in Practice
# Exercise 7.3: Creating a list of instances
# report.py

import os
import logging
from stock import Stock
from portfolio import Portfolio

# logging.basicConfig()


# Exercise 7.11: Class Methods in Practice
# Moved to 'portfolio.py' as a class method (@classmethod)
# def read_portfolio(filename, **opts):
#     '''
#     Read a stock portfolio file into a list of Stock objects.
#     '''
#     filenamepath = os.path.join(os.getcwd(), filename)
#     with open(filenamepath, 'rt') as lines:
#         holdings_dict = fileparse.parse_csv(
#             lines,
#             has_headers=True,
#             select=['name', 'shares', 'price'],
#             types=[str, int, float],
#             **opts)
# 
#     # Exercise 7.3: Creating a list of instances
#     # holdings_list = [ Stock(data['name'], data['shares'], data['price']) for data in holdings_dict] 
#     holdings_list = [ Stock(**data) for data in holdings_dict] 

#     return holdings_list

def get_portfolio(portfolio_filename):
    # Exercise 7.11: Class Methods in Practice
    # holdings_list = read_portfolio(portfolio_filename)
    # holdings_list = Portfolio.read_csv(portfolio_filename)
    # return Portfolio(holdings_list)
    filenamepath = os.path.join(os.getcwd(), portfolio_filename)
    with open(filenamepath, 'rt') as lines:
        return Portfolio.read_csv(lines)

def portfolio_cost(portfolio_filename):
    print(f'Reading portfolio (1) from "{portfolio_filename}"...')
    portfolio = get_portfolio(portfolio_filename)
    print(f'Total Value: {portfolio.total_value:.2f}')

def main(args):
    print('args: ', args)
    if(len(args) != 2):
        raise SystemExit(f'Usage: {args[0]} <portfilename>')
    portfolio_cost(args[1])

if __name__ == "__main__":
    import sys
    main(sys.argv)