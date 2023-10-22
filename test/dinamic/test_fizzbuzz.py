import pytest

import src.dinamic.fizzbuzz as dn


def test_fizzbuzz():
    num: int = 20

    print('-- FizzBuzz -- \n\n')

    dn.fizzbuzz(num)

    print('\nTest Passed!')