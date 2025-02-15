# fileparse.py (Original file: '03_fileparse_10.py')
#
# Exercise 3.3

import os
import csv
import datetime


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
        filename: str, 
        file_data_delimiter: str = ",",
        file_has_header: bool = True,
        select: list = None, 
        types: list = None,
        silence_errors: bool = False) -> list:
    '''
    Parse a CSV file into the list of records.
    '''

    # print('Parameter: filename:', filename)
    # print('Parameter: select:', select)
    # print('Parameter: types:', types)

    if select and file_has_header == False:
        raise RuntimeError("'select' argument requires column headers!")

    filenamepath = os.path.join(os.getcwd(), 'Data', filename)
    with open(filenamepath) as f:
        rows = csv.reader(f, delimiter=file_data_delimiter)

        start_rowno = 1
        selected_indices = []
        if file_has_header == True:
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
                if selected_indices:
                    row = [ row[index] for index in selected_indices ]

                if types:
                    row = [ func(data) for func, data in zip(types, row)]

                if file_has_header == True:
                    # print('row (converted): ', row)
                    record = dict(zip(selected_headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as ve:
                if silence_errors == False:
                    print(f"  >>> ValueError:: Bad Data >> Row #: {rowno}, Data: '{row}', '{ve}'")
            except Exception as ex:
                if silence_errors == False:
                    print(f"  >>> Exception:: Catch ALL Exceptions >> Type: '{type(ex).__name__}', '{ex}', Row #: {rowno}, Data: '{row}'") 

    return records
