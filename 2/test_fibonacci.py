import pytest
from solve import fib


def test_fibonacci_greater_than_zero():
    n = 20
    assert 6765 == fib(n)


def test_fibonacci_lesser_than_zero():
    n = -1
    assert "Error" in fib(n)


def test_fibonacci_long_number():
    n = 100
    assert 354224848179261915075 == fib(n)