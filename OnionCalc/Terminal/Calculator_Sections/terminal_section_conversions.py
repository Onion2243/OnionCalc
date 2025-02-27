# Import Onion Colors Library]
from Libraries.OnionColors.onioncolors import onioncolors

# Gets The Past Actions List From The Main TerminalCalculator File
from Terminal.Calculator_Sections.terminal_section_past_actions_dictionary import PastActions

# Import Python Built In Math Library
import math

# Import The Onion Calculator Functions File
from Libraries.OnionMath.functions import OnionMath

# Import Sympy And Sympy Symbols
try:
    import sympy as SymPy
except ImportError:
    print()

def Conversions_Mode():
    # Print Choices And Spacer Print
    OnionMath.spacer(1)
    print("1: Fraction To Decimal")
    print("2: Decimal To Fraction")
    print("3: Percentages")
    print("4: Metric System")
    OnionMath.spacer(1)

    # Go Back And Print Spacer
    OnionMath.spacer(1)
    print("0: Go Back")
    OnionMath.spacer(1)

    # Ask User Which Mode They Want
    mode2 = int(input("Enter the Type Of Mode: "))

    # Fraction To Decimal Mode
    if mode2 == 1:
        numerator = int(input("Enter the Numerator (Top Number) Of The Fraction: "))
        denominator = int(input("Enter the Denominator (Bottom Number) Of The Fraction: "))
        OnionMath.spacer(1)
        print("\033[92mSolution: ",OnionMath.fraction_to_decimal(numerator, denominator),"\033[0m")
        OnionMath.spacer(1)
        PastActions.append(f"Fraction To Decimal: {numerator}/{denominator} → " + str(OnionMath.fraction_to_decimal(numerator, denominator)))

    # Decimal To Fraction Mode
    if mode2 == 2:
        decimal = float(input("Enter the Decimal You Want to Convert: "))

        OnionMath.spacer(1)
        print("\033[92mSolution: ",OnionMath.decimal_to_fraction(decimal),"\033[0m")
        OnionMath.spacer(1)

        # Add The Decimal To Fraction Into The Past Calculations List
        PastActions.append(f"Fraction To Decimal: {decimal} → " + str(OnionMath.decimal_to_fraction(decimal)))

    # Percentages
    if mode2 == 3:
        # Options And Spacer Prints
        OnionMath.spacer(1)
        print("1: Decimal To Percentage")
        print("2: Fraction To Percentage")
        OnionMath.spacer(1)

        # Ask User Type Of Mode
        mode3 = int(input("Enter the Mode of Mode: "))

        # Decimal To Percentage Mode
        if mode3 == 1:
            # AsK User To Decimal
            decimal = float(input("Enter the Decimal You Want to Convert To Percentage: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.decimal_to_percent(decimal), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Decimal To Percentage: {decimal} → " + str(OnionMath.decimal_to_percent(decimal)))

        # Fraction To Percentage Mode
        if mode3 == 2:
            # Lets User Enter Numerator And Denominator
            numerator = int(input("Enter the Numerator (Top Number) Of The Fraction: "))
            denominator = int(input("Enter the Denominator (Bottom Number) Of The Fraction: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.fraction_to_percent(numerator, denominator),"\033[0m")
            OnionMath.spacer(1)

            # Add It To The Past Actions List
            PastActions.append(f"Fraction To Decimal: {numerator}/{denominator} → " + str(OnionMath.fraction_to_percent(numerator, denominator)))

    # Metric System
    if mode2 == 4:
        OnionMath.spacer(1)
        print("1: Meter To Kilometer")
        print("2: Kilometer To Meter")
        print("3: Meter To Centimeter")
        print("4: Centimeter To Meter")
        print("5: Centimeter To Millimeter")
        print("6: Millimeter To Centimeter")
        OnionMath.spacer(1)

        mode3 = int(input("Enter the Mode of Mode: "))
        OnionMath.spacer(1)

        # Meter To Kilometer
        if mode3 == 1:

            # Spacer
            OnionMath.spacer(1)

            # Ask User For Meter
            meter = float(input("Enter the Meter You Want to Convert To Kilometer: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.meter_to_kilometer(meter), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Meter To Kilometer: {meter} → " + str(OnionMath.meter_to_kilometer(meter)))

        # Kilometer To Meter
        if mode3 == 2:
            # Spacer
            OnionMath.spacer(1)

            # Ask User The Kilometer
            kilometer = float(input("Enter the Kilometer You Want to Convert To Centimeter: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.kilometer_to_meters(kilometer), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Kilometer To Meter: {kilometer} → " + str(OnionMath.kilometer_to_meters(kilometer)))

        # Meter To Centimeter
        if mode3 == 3:
            # Spacer
            OnionMath.spacer(1)

            # Ask User The Meter
            meter = float(input("Enter the Meter You Want to Convert To Centimeter: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.meter_to_centimeter(meter), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Meter To Centimeter: {meter} → " + str(OnionMath.meter_to_centimeter(meter)))

        # Centimeter To Meter
        if mode3 == 4:
            # Spacer
            OnionMath.spacer(1)

            # Ask User For Centimeter
            centimeter = float(input("Enter the Centimeter You Want to Convert To Meter: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.centimeter_to_meter(centimeter), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Centimeter To Meter: {centimeter} → " + str(OnionMath.centimeter_to_meter(centimeter)))

        # Centimeter To Millimeter
        if mode3 == 5:
            # Spacer
            OnionMath.spacer(1)

            # Ask User For Centimeter
            centimeter = float(input("Enter the Centimeter You Want to Convert To Millimeter: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.centimeter_to_millimeter(centimeter), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Centimeter To Millimeter: {centimeter} → " + str(OnionMath.centimeter_to_millimeter(centimeter)))

        # Millimeter To Centimeter
        if mode3 == 6:
            # Spacer
            OnionMath.spacer(1)

            # Ask User For Millimeter
            millimeter = float(input("Enter the Millimeter You Want to Convert To Centimeter: "))

            # Print The Solution
            OnionMath.spacer(1)
            print("\033[92mSolution: ", OnionMath.millimeter_to_centimeter(millimeter), "\033[0m")
            OnionMath.spacer(1)

            # Add The Decimal To Fraction Into The Past Calculations List
            PastActions.append(f"Millimeter To Centimeter: {millimeter} → " + str(OnionMath.millimeter_to_centimeter(millimeter)))