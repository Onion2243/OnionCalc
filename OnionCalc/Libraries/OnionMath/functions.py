# Import Needed Libraries
from fractions import Fraction

# Includes All My Custom Math Library Functions
class OnionMath:
    # Add Function, Takes In 2 Ints Or Floating Point Values
    def add(num1, num2):
        return num1 + num2

    # Subtract Function, Takes In 2 Ints Or Floating Point Values
    def subtract(num1, num2):
        print("")
        return num1 - num2

    # Multiply Functions, Takes In 2 Ints Or Floating Point Values
    def multiply(num1, num2):
        print("")
        return num1 * num2

    # Divide Functions, Takes In 2 Ints Or Floating Point Values
    def divide(num1, num2):
        print("")
        return num1 / num2

    # Exponential Powers Function, Takes In A Number And A Exponent As Integers Or Floats
    def powers(num, exponent):
        return num ** exponent

    # Fraction To Decimal, Takes A Numerator Int Value and a Denominator Int Value
    def fraction_to_decimal(numerator, denominator):
        return numerator / denominator

    # Function To Convert Decimal To Fraction, Takes In Decimal Float Point Value
    def decimal_to_fraction(decimal):
        return Fraction(decimal)
    def decimal_to_percent(decimal):
        return decimal * 100

    def fraction_to_percent(numerator, denominator):
        decimal = numerator / denominator
        return decimal * 100
    def spacer(amount_of_spaces):
        for i in range(amount_of_spaces):
            print("")
            
    # Metric System Conversion Functions
    def meter_to_kilometer(meter):
        return meter / 1000
    def kilometer_to_meters(kilometer):
        return kilometer * 1000
    def meter_to_centimeter(meter):
        return meter * 100
    def centimeter_to_meter(centimeter):
        return centimeter / 100
    def centimeter_to_millimeter(centimeter):
        return centimeter * 10
    def millimeter_to_centimeter(millimeter):
        return millimeter / 10
