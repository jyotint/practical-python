# Exercise 8.1: Writing Unit Tests

# test_stock_unittest.py

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('MSFT', 100, 101.6)
        self.assertEqual(s.name, 'MSFT')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 101.6)

    def test_bad_shares(self):
        s = Stock('MSFT', 100, 101.6)
        # with self.assertRaises(ValueError):
        with self.assertRaises(TypeError):
            s.shares = 'bad data'

    def test_cost(self):
        s = Stock('MSFT', 100, 101.6)
        self.assertEqual(s.cost, 10160.00)

    def test_sell(self):
        s = Stock('MSFT', 100, 101.6)
        s.sell(25)
        self.assertEqual(s.shares, 75)
        self.assertEqual(s.cost, 75*101.6)

if __name__ == '__main__':
    unittest.main()
