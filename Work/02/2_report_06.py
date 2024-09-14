# Exercise 2.6: Dictionaries as a container
# 'Data/prices.csv'

import os
import sys
import csv

def read_prices(filename):
    f = open(os.path.join(os.getcwd(), 'Data', filename), 'rt')
    rows = csv.reader(f)

    # No header in this prices.csv, so skipping it
    # headers = next(rows)

    prices = {}
    for row in rows:
        try:
            name = row[0]
            quantity = float(row[1])

            prices[name] = quantity
            print("Row Added: ", name, quantity)
        except ValueError:
            print('  >>> ValueError: Invalid row', row)
        except Exception as ex:
            print(f"  >>> Catch ALL Exceptions >> Type: '{ex}', Invalid Row: '{row}'") 

    print(prices)
    return prices


if(sys.argv == 2):
    filename = sys.argv[1]
else:
    filename = 'prices.csv'

prices = read_prices(filename)
