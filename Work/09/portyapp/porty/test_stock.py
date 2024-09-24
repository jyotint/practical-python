# Exercise 8.1: Writing Unit Tests

# test_stock_unittest.py

import pytest
from .stock import Stock

def test_stock_create():
    s = Stock('MSFT', 100, 101.6)
    assert s.name == 'MSFT'
    assert s.shares == 100
    assert s.price == 101.6

def test_stock_cost():
    s = Stock('MSFT', 100, 101.6)
    assert s.cost == 100*101.6

def test_stock_sell():
    s = Stock('MSFT', 100, 101.6)
    s.sell(25)
    assert s.shares == 75
    assert s.cost == 75*101.6

def test_stock_name_bad_data():
    s = Stock('MSFT', 100, 101.6)
    # with pytest.raises(ValueError):
    with pytest.raises(TypeError):
        s.name = 10

def test_stock_shares_bad_data_str():
    s = Stock('MSFT', 100, 101.6)
    with pytest.raises(TypeError):
        s.shares = 'bad data'

def test_stock_shares_bad_data_float():
    s = Stock('MSFT', 100, 101.6)
    with pytest.raises(TypeError):
        s.shares = 201.1

def test_stock_price_bad_data_str():
    s = Stock('MSFT', 100, 101.6)
    with pytest.raises(TypeError):
        s.price = 'bad data'

def test_stock_repr():
    s = Stock('MSFT', 100, 101.6)
    assert repr(s) == "Stock('MSFT', 100, 101.60)"

def test_stock_str():
    s = Stock('MSFT', 100, 101.6)
    assert str(s) == "Stock(name: 'MSFT', shares: 100, price: 101.60)"