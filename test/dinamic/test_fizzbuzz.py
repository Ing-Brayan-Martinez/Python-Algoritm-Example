import pytest

from src.dinamic.fizzbuzz import fizzbuzz


def test_fizzbuzz():
    num: int = 20

    print('-- FizzBuzz -- \n\n')

    fizzbuzz(num)

    print('\nTest Passed!')