# Exercise 8.1: Writing Unit Tests

# test_stock_unittest.py

from stock import Stock

def test_create():
    s = Stock('MSFT', 100, 101.6)
    assert s.name == 'MSFT'
    assert s.shares == 100
    assert s.price == 101.6

# def test_bad_shares():
#     s = Stock('MSFT', 100, 101.6)
#     # with self.assertRaises(ValueError):
#     with self.assertRaises(TypeError):
#         s.shares = 'bad data'

def test_cost():
    s = Stock('MSFT', 100, 101.6)
    assert s.cost == 10160.00

def test_sell():
    s = Stock('MSFT', 100, 101.6)
    s.sell(25)
    assert s.shares == 75
    assert s.cost == 75*101.6
