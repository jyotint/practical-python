# report.py
#
# Exercise 2.4
import os

f = open(os.path.join(os.getcwd(), 'Data', 'portfolio.csv'), 'rt')
headers = next(f).split(',')
print(headers)

for line in f:
    row = line.split(',')
    print(row)

f.close()
