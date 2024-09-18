# Exercise 7.8: Simplifying Function Calls

# typedproperty2.py

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


TypedString = lambda name: typedproperty(name, str)
TypedInt = lambda name: typedproperty(name, int)
TypedFloat = lambda name: typedproperty(name, float)


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

    class Stock03(StockBase):
        name = TypedString('name')
        shares = TypedInt('shares')
        price = TypedFloat('price')

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
            self.self_name = "Stock03"


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

    try:
        s31 = Stock03('s31-1', 31, 31.31)
        print(s31)
        s31.shares = 'bad data'
        print(s31)
    except Exception as ex:
        print(f'EXCEPTION: s31: "{ex}"')
