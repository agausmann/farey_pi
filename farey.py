"""
Implementation of a rational approximation algorithm using Farey sequences.
"""

from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from typing import Iterator

def farey(num: Decimal) -> Iterator[Fraction]:
    """
    An iterator over successive approximations of the given number, generated
    using Farey sequences.
    """

    # In the video, Matt set the initial bounds to 0 and 1 and only compared
    # the fractional part, adding the integer part later. Here, I've decided to
    # set the bounds to the floor/ceiling of the given value, which allows me
    # to compare and converge on the given value itself. This should have the
    # same behavior as Matt's algorithm for all of the test cases.
    lower = Fraction(num.to_integral_value(ROUND_FLOOR))
    upper = Fraction(num.to_integral_value(ROUND_CEILING))
    
    while True:
        appx = Fraction(
            lower.numerator + upper.numerator,
            lower.denominator + upper.denominator,
        )

        if appx < num:
            lower = appx
        else:
            upper = appx

        yield appx


def test_data():
    """
    Tests the implementation of the Farey apprximation algorithm, proving that they
    eventually provide the given approximation for each example in
    `approximations.csv`.
    """

    import data

    for test_case in data.approximations:
        print('{} ?  '.format(test_case), end='')

        # Convert the LHS fraction to a decimal.
        lhs = test_case.lhs
        lhs = Decimal(lhs.numerator) / Decimal(lhs.denominator)

        # Divide both sides by pi, RHS should be a generated rational approximation of LHS.
        lhs /= data.PI
        rhs = test_case.rhs_frac # (already missing a factor of pi, by definition)

        for appx in farey(lhs):
            if appx == rhs:
                print('OK')
                break

            if appx.denominator >= rhs.denominator:
                print('FAIL')
                raise Exception('Expected {}, got {}'.format(rhs, appx))


if __name__ == '__main__':
    test_data()
