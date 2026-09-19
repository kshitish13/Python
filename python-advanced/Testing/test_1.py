
def add(a,b):
    return a+b

#testing Function
def test_add():
    assert add(1,2) == 3
    assert add(-1,-3) == -4

def test_add_big_number():
    assert add(2000000,3000000) == 5000000