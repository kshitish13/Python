import pytest

def multiply(a,b):
    return a**b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError
    return a/b

def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(5,0) == 0

def test_divide():
    assert divide(12,6) == 2
    with pytest.raises(ZeroDivisionError):
        divide(12,0)

