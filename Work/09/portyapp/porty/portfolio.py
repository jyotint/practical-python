from . import fileparse
from .stock import Stock 

# One important observation about this–generally code is considered “Pythonic” 
# if it speaks the common vocabulary of how other parts of Python normally work. 
# 
# For "Container" objects, supporting iteration, indexing, containment, and 
# other kinds of operators is an important part of this.

class Portfolio:
    __slots__ = ('_holdings')

    def __init__(self):
        self.holdings: list[Stock] = []

    def __str__(self):
        return f'Portfolio(Stocks >> count: {len(self)}, total_value: {self.total_value:.2f})'

    def __repr__(self):
        return f'Portfolio({self.holdings})'

    def __len__(self):
        return len(self.holdings)

    def __contains__(self, name: str):
        return any( s.name == name for s in self.holdings )     # A generator expression

    def __iter__(self):
        return self.holdings.__iter__()

    def __getitem__(self, key: int) -> Stock:
        return self.holdings[int(key)]

    def __setitem__(self, key: int, value: Stock) -> None:
        self.holdings[int(key)] = value

    def __delitem__(self, key: int) -> None:
        del self.holdings[int(key)]

    def find(self, name: str) -> Stock | None:
        stock_list = [ s for s in self.holdings if s.name == name ] # A list comprehension
        if len(stock_list) == 0:
            return None
        else:
            return stock_list[0]

    def append(self, value: Stock):
        self.holdings.append(value)

    def update(self, other: Stock):
        stock = self.find(other.name)
        stock.copy_from(other)

    def copy_from(self, other: Stock):
        if other != None and isinstance(other, Stock):
            self.shares = other.shares
            self.price = other.price

    # FIXME Using something like C# "nameof"
    def copy(self, **kwargs):
        if kwargs != None:
            if 'shares' in self:
                self.shares = kwargs['shares']
            if 'price' in self:
                self.price = kwargs['price']

    @property
    def holdings(self) -> list[Stock]:
        return self._holdings
    
    @holdings.setter
    def holdings(self, value: list[Stock]):
        # Error check ????
        self._holdings = value

    @property
    def total_value(self) -> float:
        return sum( s.cost for s in self.holdings )         # A generator expression

    @classmethod
    def read_csv(cls, lines, **opts):
        '''
        Read a stock portfolio into a list of Stock objects.
        '''
        self = cls()

        holdings_dict, errored_records = fileparse.parse_csv(
            lines,
            has_headers=True,
            select=['name', 'shares', 'price'],
            types=[str, int, float],
            **opts)

        for holding in holdings_dict:
            self.append(Stock(**holding))

        return self
