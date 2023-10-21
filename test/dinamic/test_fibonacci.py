import pytest

from src.dinamic.fibonacci import fibonacci


def test_fibonacci():
    num: int = 20
    expectedValue: int = 6765

    resultValue: int = fibonacci(num)

    print('-- Fibonacci -- \n\n')

    print(f'Fibonacci of {num}  is {resultValue} \n\n')

    assert expectedValue == resultValue

    print('Test Passed!')