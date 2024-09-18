# Exercise 7.7: Using Closures to Avoid Repetition

# typedproperty1.py

def typedproperty(name: str, expected_type: type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)
    
    @prop.setter
    def prop(self, value):
        # print(f'typed_property()::@prop.setter: "{private_name}", "{expected_type}", "{value}"')
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected "{expected_type}" type!')
        setattr(self, private_name, value)

    return prop


if __name__ == '__main__':
    class StockBase:
        def __repr__(self):
            return f"Stock('{self.self_name}', '{self.name}', {self.shares}, {self.price})"

        def __str__(self):
            return f"Stock('{self.self_name}', name: '{self.name}', shares: {self.shares}, price: {self.price})"

    class Stock01(StockBase):
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
            self.self_name = "Stock01"

    class Stock02(StockBase):
        name = typedproperty('name', str)
        shares = typedproperty('shares', int)
        price = typedproperty('price', float)

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
            self.self_name = "Stock02"

    try:
        s11 = Stock01('s11-1', 11, 11.11)
        print(s11)
        s11.shares = 'bad data'
        print(s11)
    except Exception as ex:
        print(f'EXCEPTION: s11: "{ex}"')

    try:
        s21 = Stock02('s21-1', 21, 21.21)
        print(s21)
        s21.shares = 'bad data'
        print(s21)
    except Exception as ex:
        print(f'EXCEPTION: s21: "{ex}"')
