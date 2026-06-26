#Value Error Example
import pytest
import math
def calculate_square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def test_calculate_square_root():

    assert calculate_square_root(4) == 2.0

    assert calculate_square_root(0) == 0.0

    with pytest.raises(ValueError):
        calculate_square_root(-1) 

#Type Error Example
import pytest
def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5

    assert add("Hello, ", "World!") == "Hello, World!"

    with pytest.raises(TypeError):
        add(2, "3") 

#Zero Division Error Example
import pytest 
def divide(a,b):
    return a/b

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10,0) 

# Key Error Example
import pytest
def get_value(d, key):
    return d[key]

def test_get_value():
    with pytest.raises(KeyError):
        get_value({"a": 1, "b": 2}, "c") 


