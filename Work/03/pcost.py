# Exercise 3.15: main() functions
# Exercise 3.16: Making Scripts

import sys
from report import read_portfolio

csv_col_name = 'name'
csv_col_date = 'date'
csv_col_shares = 'shares'
csv_col_price = 'price'

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)

    total = 0.0
    for data in portfolio:
        total += data[csv_col_shares] * data[csv_col_price]
    return total

def main(args: list):
    print('args: ', args)
    if(len(args) != 2):
        raise SystemExit(f'Usage: {args[0]} <portfoliofile>')

    price_filename = args[1]
    cost = portfolio_cost(price_filename)
    print(f'Portfolio Cost: {cost:>10.2f}')

if __name__ == "__main__":
    main(sys.argv)
