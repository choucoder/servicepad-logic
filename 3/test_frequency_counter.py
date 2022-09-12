import pytest
from solve import frequency_counter


def test_frequency_counter():
    text = "Hola como estas?. Hola bien y tu"
    freq = {'hola': 2, 'como': 1, 'estas': 1, 'bien': 1, 'y': 1, 'tu': 1}
    
    assert freq == frequency_counter(text)
