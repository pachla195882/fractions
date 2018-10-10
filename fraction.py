"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fragion` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (ValueError if not),
- method `value` returning float value of the fraction.
"""
from math import gcd


class Fraction(object):
    """
    Fraction class.
    """

    def __init__(self, numerator, denominator):
        greatestCommonDivisor = gcd(numerator, denominator)
        self.numerator = int(numerator / gcd(abs(numerator), abs(denominator)))
        self.denominator = int(denominator / gcd(abs(numerator), abs(denominator)))
        if self.denominator < 0:

            self.denominator *= -1
            self.numerator *= -1
        elif self.denominator == 0:

            raise ValueError

    def value(self):
        result = (self.numerator) / (self.denominator)
        return result

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return "%s/%s" % (self.numerator, self.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator