# Exercise 7.7: Using Closures to Avoid Repetition

# typedproperty.py

def typed_property(name: str, expected_type: type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)
    
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected "{expected_type}" type!')
        setattr(self, private_name, value)

    return prop


TypedString = lambda name: typed_property(name, str)
TypedInt = lambda name: typed_property(name, int)
TypedFloat = lambda name: typed_property(name, float)
