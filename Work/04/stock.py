# stock.py

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price

    def __str__(self) -> str:
        '''
        # Exercise 4.9: Better output for printing objects
        
        Used with `str()` and `print()`
        '''
        return f"Stock(name: '{self.name}', shared: {self.shares}, price: {self.price:.2f})"

    def __repr__(self) -> str:
        '''
        # Exercise 4.9: Better output for printing objects
        Used with `repr()`

        Note: The convention for __repr__() is to return a string that, 
                when fed to eval(), will recreate the underlying object. 
                If this is not possible, some kind of easily readable 
                representation is used instead.
        '''
        return f"Stock('{self.name}', {self.shares}, {self.price:.2f})"

    def cost(self) -> float:
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares) -> None:
        '''
        Sell a number of shares
        '''
        self.shares -= nshares

