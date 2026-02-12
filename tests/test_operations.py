from src.math_operations import addition, subtraction

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_subtraction():
    assert subtraction(5, 2) == 3
    assert subtraction(0, 1) == -1
    assert subtraction(10, 5) == 5