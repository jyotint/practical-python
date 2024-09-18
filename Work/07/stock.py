# Exercise 7.9: Putting it into practice

# stock.py

from typedproperty import TypedInt, TypedFloat, TypedString, typed_property


class Stock:
    # Exercise 5.8: Adding slots
    # It should be noted that __slots__ is most commonly used as an optimization 
    #       on classes that serve as data structures. Using slots will make such 
    #       programs use far-less memory and run a bit faster. 
    #       You should probably avoid __slots__ on most other classes however.
    # The following errors out due to Getter and Setter decorators.
    # __slots__ = ('name', 'shares', 'price') 
    # __slots__ = ('name', '_shares', 'price')

    # Exercise 7.9: Putting it into practice
    name = TypedString('name')
    shares = TypedInt('shares')
    price = TypedFloat('price')

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
        return f"Stock(name: '{self.name}', shares: {self.shares}, price: {self.price:.2f})"

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

    # Using typed_property() now
    # Exercise 5.7: Properties and Setters (see "Exercise 7.9: Putting it into practice")
    # @property
    # def shares(self) -> int:
    #     return self._shares
    
    # # Exercise 5.7: Properties and Setters
    # @shares.setter
    # def shares(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError('Expected "int" type!')
    #     self._shares = value

    @property
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

