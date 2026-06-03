# import pytest
from calculator import add,sub,mul,div


def test_add():
    assert add(4, 5) == 9
    assert add(1, 2) == 3
    assert add(0, 0) == 0

def test_sub():
    assert sub(4, 5) == -1
    assert sub(2, 1) == 1
    assert sub(0, 0) == 0

def test_mul():
    assert mul(4, 5) == 20
    assert mul(2, 3) == 6
    assert mul(0, 5) == 0

def test_div():
    assert div(10, 2) == 5
    assert div(9, 3) == 3
    try:
        div(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
