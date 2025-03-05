import pytest
from is_prime import is_prime

@pytest.mark.parametrize(
    "number,expected",[
        (1,False),
        (2,True),
        (8,False),
        (11,True),
        (25,False),
        (28,False),
        (29,True),
        (49,False),
        (51,False),
        (53,True),
        (121,False),
        (125,False),
        (127,True)
    ])

def test_is_prime(number,expected):
    assert is_prime(number) == expected