# pcost.py
#
# Exercise 1.27
import os
import sys


def portfolio_cost(filename):
    # f = open(os.path.join(os.getcwd(), 'Data', 'missing.csv'), 'rt')
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    headers = next(f).split(',')
    print(headers)

    cost = 0.0
    for line in f:
        try:
            row = line.split(',')
            print(row)
            quantity = int(row[1])
            unit_cost = float(row[2])
            cost += quantity * unit_cost
        except ValueError:
            print('Could not parse', line)
        # except Exception as ex:
        #     print(f"Catch ALL Exceptions >> Type: '{ex}', Invalid Row: '{line}'") 

    f.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost is {cost}')
