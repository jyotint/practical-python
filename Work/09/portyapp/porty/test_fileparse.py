import pytest
from .fileparse import parse_csv


@pytest.fixture
def example_lines_with_header():
    list = []
    list.append('name,date,time,shares,price')
    for r in example_data_lines():
        list.append(r)
    return list

@pytest.fixture
def example_lines_with_header_and_bad_data():
    list = []
    list.append('name,date,time,shares,price')
    for r in example_data_lines(introduce_bad_data=True):
        list.append(r)
    return list

@pytest.fixture
def example_lines_without_header():
    return example_data_lines()

@pytest.fixture
def example_lines_without_header_and_bad_data():
    return example_data_lines(introduce_bad_data=True)

def example_data_lines(introduce_bad_data=False):
    list = []
    list.append('"AA","6/11/2007","9:50am",100,32.20')
    list.append('"IBM","5/13/2007","4:20pm",50,91.10')
    list.append('"CAT","9/23/2006","1:30pm",150,83.44')
    list.append('"MSFT","5/17/2007","10:30am",200,51.23')
    list.append('"GE","2/1/2006","10:45am",95,40.37')
    list.append('"MSFT","10/31/2006","12:05pm",50,65.10')
    list.append('"IBM","7/9/2006","3:15pm",100,70.44')
    if introduce_bad_data == True:
        list[4] = '"GE","","10:45am",,40.37'     # no date, no shares
    return list


def test_fileparse_parse_csv_with_all_defaults(example_lines_with_header):
    example_data = example_lines_with_header
    example_data_length = len(example_data)-1     # -1 due to header
    resultset_number_of_columns = 5

    records, errored_records = parse_csv(example_data)
    # print(example_lines)
    # print(records)
    assert len(records) == example_data_length

    record = records[0]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'AA'
    assert record['date'] == '6/11/2007'
    assert record['time'] == '9:50am'
    assert record['shares'] == '100'
    assert record['price'] == '32.20'

    record = records[3]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'MSFT'
    assert record['date'] == '5/17/2007'
    assert record['time'] == '10:30am'
    assert record['shares'] == '200'
    assert record['price'] == '51.23'


def test_fileparse_parse_csv_with_selected_columns(example_lines_with_header):
    example_data = example_lines_with_header
    example_data_length = len(example_data)-1     # -1 due to header
    selected_columns=['name', 'shares', 'price']
    resultset_number_of_columns = len(selected_columns)

    records, errored_records = parse_csv(example_data, select=selected_columns)
    assert len(records) == example_data_length

    record = records[0]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'AA'
    assert record['shares'] == '100'
    assert record['price'] == '32.20'

    record = records[3]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'MSFT'
    assert record['shares'] == '200'
    assert record['price'] == '51.23'


def test_fileparse_parse_csv_with_selected_columns_and_type(example_lines_with_header):
    example_data = example_lines_with_header
    example_data_length = len(example_data)-1     # -1 due to header
    selected_columns=['name', 'shares', 'price']
    column_types=[str, int, float]
    resultset_number_of_columns = len(selected_columns)

    records, errored_records = parse_csv(example_data, select=selected_columns, types=column_types)
    assert len(records) == example_data_length

    record = records[0]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'AA'
    assert record['shares'] == 100
    assert record['price'] == 32.20

    record = records[3]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'MSFT'
    assert record['shares'] == 200
    assert record['price'] == 51.23

def test_fileparse_error_should_not_be_string():
    with pytest.raises(RuntimeError) as ex:
        _ = parse_csv('test.csv')
    assert str(ex.value) == '"lines" should not be string!'

def test_fileparse_error_should_be_iterable():
    with pytest.raises(RuntimeError) as ex:
        _ = parse_csv(12)
    assert str(ex.value) == '"lines" should be iterable!'


def test_fileparse_error_no_headers_should_not_pass_select_columns(example_lines_without_header):
    example_data = example_lines_without_header
    selected_columns=['name', 'shares', 'price']

    with pytest.raises(RuntimeError) as ex:
        _ = parse_csv(example_data, has_headers=False, select=selected_columns)
    assert str(ex.value) == '"select" argument requires column headers!'


def test_fileparse_no_headers_csv_should_return_list_of_tuples(example_lines_without_header):
    example_data = example_lines_without_header
    example_data_length = len(example_data)     # no headers
    resultset_number_of_columns = 5

    records, errored_records = parse_csv(example_data, has_headers=False)
    # print(example_lines)
    # print(records)
    assert len(records) == example_data_length

    record = records[0]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type(())
    assert record[0] == 'AA'
    assert record[1] == '6/11/2007'
    assert record[2] == '9:50am'
    assert record[3] == '100'
    assert record[4] == '32.20'

    record = records[3]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type(())
    assert record[0] == 'MSFT'
    assert record[1] == '5/17/2007'
    assert record[2] == '10:30am'
    assert record[3] == '200'
    assert record[4] == '51.23'


def test_fileparse_parse_csv_with_selected_columns_and_type_with_bad_data(example_lines_with_header_and_bad_data):
    example_data = example_lines_with_header_and_bad_data
    example_data_length = len(example_data)-1     # -1 due to header
    selected_columns=['name', 'shares', 'price']
    column_types=[str, int, float]
    resultset_number_of_columns = len(selected_columns)

    records, errored_records = parse_csv(example_data, select=selected_columns, types=column_types)
    assert len(errored_records) > 0
    errored_record = errored_records[0]
    ex = errored_record['ex']
    assert str(ex).startswith("invalid literal for int() with base 10")


def test_fileparse_parse_csv_with_selected_columns_and_type_with_bad_data_with_log_errors(example_lines_with_header_and_bad_data):
    example_data = example_lines_with_header_and_bad_data
    example_data_length = len(example_data) - 1 - 1     # -1 due to header, -1 for bad data
    selected_columns=['name', 'shares', 'price']
    column_types=[str, int, float]
    resultset_number_of_columns = len(selected_columns)

    records, errored_records = parse_csv(example_data, select=selected_columns, types=column_types, log_errors=True)
    assert len(records) == example_data_length
    assert len(errored_records) == 1

    record = records[0]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'AA'
    assert record['shares'] == 100
    assert record['price'] == 32.20

    record = records[3]
    assert len(record) == resultset_number_of_columns
    assert type(record) == type({})
    assert record['name'] == 'MSFT'
    assert record['shares'] == 200
    assert record['price'] == 51.23
