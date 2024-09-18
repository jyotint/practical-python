# Exercise 6.2: Supporting Iteration
# portfolio.py

import fileparse
from stock import Stock 

# One important observation about this–generally code is considered “Pythonic” 
# if it speaks the common vocabulary of how other parts of Python normally work. 
# 
# For "Container" objects, supporting iteration, indexing, containment, and 
# other kinds of operators is an important part of this.


class Portfolio:
    __slots__ = ('_holdings')

    def __init__(self, holdings: list[Stock]):
        self.holdings: list[Stock] = holdings

    def __str__(self):
        return f'Portfolio(Stocks >> count: {len(self)}, total_value: {self.total_value:.2f})'

    def __repr__(self):
        return f'Portfolio({self.holdings})'

    def __len__(self):
        return len(self.holdings)

    def __contains__(self, name: str):
        # return any( [s.name == name for s in self.holdings] ) # A list comprehension
        return any( s.name == name for s in self.holdings )     # A generator expression

    def __iter__(self):
        return self.holdings.__iter__()

    def __getitem__(self, key: int) -> Stock:
        return self.holdings[int(key)]

    def __setitem__(self, key: int, value: Stock) -> None:
        self.holdings[int(key)] = value

    def __delitem__(self, key: int) -> None:
        del self.holdings[int(key)]

    def find(self, name: str) -> Stock:
        stock_list = [ s for s in self.holdings if s.name == name ] # A list comprehension
        return stock_list[0]

    @property
    def holdings(self) -> list[Stock]:
        return self._holdings
    
    @holdings.setter
    def holdings(self, value: list[Stock]):
        # Error check ????
        self._holdings = value

    @property
    def total_value(self) -> float:
        # return sum( [s.cost for s in self.holdings] )     # A list comprehension
        return sum( s.cost for s in self.holdings )         # A generator expression
