# Import Needed Libraries
from fractions import Fraction
from Libraries.OnionColors.onioncolors import onioncolors

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

    def thank_you_message(self):
        # Prints Thanks For Using Message
        print(f"""

        Thank You For Using
        {onioncolors.text_color("orange")}                        
        ------------------------------------------------------------------------------------------------
                                        ALGEBRAIC CALCULATOR V.0.1.0
        ------------------------------------------------------------------------------------------------
        """, "\033[0m")

    def decimal_to_percent(decimal):
        return decimal * 100

    def fraction_to_percent(numerator, denominator):
        decimal = numerator / denominator
        return decimal * 100
    
    def spacer(amount_of_spaces):
        for i in range(amount_of_spaces):
            print("")

