import pytest

from src.dinamic.factorial import factorial


def test_factorial():
    num: int = 5
    expectedValue: int = 120

    resultValue: int = factorial(num)

    print('-- Factorial -- \n\n')

    print(f'Factorial of {num}  is {resultValue} \n\n')

    assert expectedValue == resultValue

    print('Test Passed!')

