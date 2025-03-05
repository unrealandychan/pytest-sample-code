from main import add, divide
import pytest

def test_add():
    assert add(1,2) == 3 ,"1+2 should be 3"
    assert add(1,-1) == 0 ,"1+(-1) should be 0"
    assert add(1,0) == 1 ,"1+0 should be 1"

def test_divide():
    with pytest.raises(ValueError) as e:
        divide(10,0)
    assert str(e.value) == "division by zero"
