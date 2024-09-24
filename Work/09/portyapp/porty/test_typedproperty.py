import pytest
from .typedproperty import typed_property, TypedString, TypedInt, TypedFloat


class ATestClass:
    stringData = TypedString('stringData')
    intData = TypedInt('intData')
    floatData = TypedFloat('floatData')
    boolData =  typed_property('boolData', bool)

    def __init__(self, stringData, intData, floatData, boolData):
        self.stringData = stringData
        self.intData = intData
        self.floatData = floatData
        self.boolData = boolData


@pytest.fixture
def example_ATestClass():
    return ATestClass('string data', 11, 22.22, False)


def test_typedproperty_TypedString(example_ATestClass):
    example_ATestClass.stringData = 'new string data'
    assert example_ATestClass.stringData == 'new string data'

def test_typedproperty_TypedString_int(example_ATestClass):
    with pytest.raises(TypeError):
        example_ATestClass.stringData = 101


def test_typedproperty_TypedInt(example_ATestClass):
    example_ATestClass.intData = 101
    assert example_ATestClass.intData == 101

def test_typedproperty_TypedInt_str(example_ATestClass):
    with pytest.raises(TypeError):
        example_ATestClass.intData = 'string data'


def test_typedproperty_TypedFloat(example_ATestClass):
    example_ATestClass.floatData = 201.7
    assert example_ATestClass.floatData == 201.7

def test_typedproperty_TypedFloat_str(example_ATestClass):
    with pytest.raises(TypeError):
        example_ATestClass.floatData = 'string data'


def test_typedproperty_TypedBool(example_ATestClass):
    example_ATestClass.boolData = True
    assert example_ATestClass.boolData == True

def test_typedproperty_TypedBool_str(example_ATestClass):
    with pytest.raises(TypeError):
        example_ATestClass.boolData = 'string data'

