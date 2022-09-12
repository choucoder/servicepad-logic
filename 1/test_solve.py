import pytest
from solve import solve


def test_multiples_of_three():
    n = 3
    assert "fizz" == solve(n)


def test_multiples_of_five():
    n = 5
    assert "buzz" == solve(n)


def test_multiples_of_three_and_five():
    n = 15
    assert "fizz buzz" == solve(n)