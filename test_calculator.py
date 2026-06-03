# import pytest
from calculator import add,sub

def test_add():
    assert add(4, 5) == 9
    assert add(1, 2) == 3
    assert add(0, 0) == 0

def test_sub():
    assert sub(4, 5) == -1
    assert sub(2, 1) == 1
    assert sub(0, 0) == 0
