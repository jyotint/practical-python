# Exercise 3.10: Silencing Errors
# 'Data/portfolio.csv'
# 'Data/missing.csv'
# 'Data/portfoliodate.csv'
# 'Data/portfolio.csv'

import csv
import datetime
from collections.abc import Iterable


def convert_str_to_date_object(data):
    dateObject = datetime.date(1970, 1, 1)
    datetimeObject = datetime.datetime.strptime(data, '%m/%d/%Y')
    dateObject = datetime.date(datetimeObject.year, datetimeObject.month, datetimeObject.day)
    return dateObject

def convert_str_to_time_object(data):
    dateObject = datetime.date(1970, 1, 1)
    datetimeObject = datetime.datetime.strptime(data, '%I:%M%p')
    dateObject = datetime.time(datetimeObject.hour, datetimeObject.minute, datetimeObject.second)
    return dateObject


def parse_csv(
        lines, #01 filename,
        file_data_delimiter: str = ",",
        has_headers: bool = True,
        select: list = None, 
        types: list = None,
        silence_errors: bool = False) -> list:
    '''
    Parse a CSV file into the list of records with type conversion.
    '''

    # print('Parameter: filename:', filename)
    # print('Parameter: file_data_delimiter:', file_data_delimiter)
    # print('Parameter: file_has_header:', file_has_header)
    # print('Parameter: select:', select)
    # print('Parameter: types:', types)
    # print('Parameter: silence_errors:', silence_errors)

    # print('type(lines): ', type(lines))
    # print('hasattr(lines, __iter__)', hasattr(lines, '__iter__'))
    # if not isinstance(lines, Iterable):   # str as well as lines are iterable
    if isinstance(lines, str):
        raise RuntimeError("'lines' should be an iterable and not string!")
    if not isinstance(lines, Iterable):
        raise RuntimeError("'lines' should be iterable!")

    if select and not has_headers:
        raise RuntimeError("'select' argument requires column headers!")

    #01 filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    #01 with open(filenamepath) as f:
    rows = csv.reader(lines, delimiter=file_data_delimiter)

    start_rowno = 1
    selected_indices = []
    if has_headers == True:
        # Read file header
        selected_headers = next(rows)
        start_rowno += 1

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            selected_indices = [ selected_headers.index(colname) for colname in select ]
            selected_headers = select

    records = []
    for rowno, row in enumerate(rows, start=start_rowno):
        if not row:     # Skip row with no data
            continue

        try:
            # If specific column indices are selected, pick them out
            if selected_indices:
                row = [ row[index] for index in selected_indices ]

            # Apply type conversion to the row
            if types:
                row = [ func(data) for func, data in zip(types, row)]

            # Make a dictionary (if it has headers) or make a tuple 
            if has_headers == True:
                record = dict(zip(selected_headers, row))
            else:
                record = tuple(row)
            records.append(record)

        except ValueError as ve:
            if not silence_errors:
                print(f"  >>> ValueError:: Bad Data >> Row #: {rowno}, Data: '{row}', '{ve}'")
        except Exception as ex:
            if not silence_errors:
                print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{type(ex).__name__}', '{ex}', Row #: {rowno}, Data: '{row}'") 

    return records
