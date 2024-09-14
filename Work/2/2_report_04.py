# Exercise 2.4: A list of tuples
# 'Data/portfolio.csv'
# 'Data/missing.csv'

import os
import sys
import csv

def read_portfolio(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    headers = next(rows)
    portfolio = []
    for row in rows:
        try:
            quantity = int(row[1])
            unit_cost = float(row[2])
            data = (row[0], quantity, unit_cost)
            portfolio.append(data)
        except ValueError:
            print('  >>> Invalid row', row)
        except Exception as ex:
            print(f"  >>> Catch ALL Exceptions >> Type: '{ex}', Invalid Row: '{row}'") 

    return portfolio

def portfolio_cost(portfolio):
    total = 0.0
    for name, quantity, unit_cost in portfolio:
        total += quantity * unit_cost
    return total

# if(sys.argv == 2):
#     filename = sys.argv[1]
# else:
#     filename = 'portfolio.csv'

# portfolio = read_portfolio(filename)

