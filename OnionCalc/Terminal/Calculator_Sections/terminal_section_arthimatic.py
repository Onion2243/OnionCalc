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

def Arthmatic_Mode():

    print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Opening Arithmatic Calculator
------------------------------------------------------------------------------------------------
\033[0m
""",)

    # Spacer Print
    OnionMath.spacer(1)

    # Print Choices
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exponents")
    print("6: Square Root")

    # Go Back And Print Spacer
    OnionMath.spacer(1)
    print("0: Go Back")

    # Spacer Print
    OnionMath.spacer(1)

    Mode2 = int(input("Enter The Type Of Mode: "))

    # Spacer Print
    OnionMath.spacer(1)

    # Addition Mode
    if Mode2 == 1:

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Both Numbers To Add Together
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))

        # Run Add Function
        OnionMath.spacer(1)
        print(f"\033[32mSolution: {OnionMath.add(num1, num2)} \033[0m")
        OnionMath.spacer(1)

        # Insert Solution And Type Into The List
        PastActions.append(f"Addition: {num1} + {num2} = " + str(OnionMath.add(num1, num2)))

    # Subtraction Mode
    if Mode2 == 2:

        # Spacer Print
        OnionMath.spacer(1)

        # Tells User To Enter Bigger Number First
        print("\033[91mNOTE: PLEASE ENTER BIGGER NUMBER FIRST THEN SMALLER NUMBER LAST \033[0m")

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Both Numbers To Subtract Together
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))

        # Run Subtraction Function
        OnionMath.spacer(1)
        print(f"\033[32mSolution: {OnionMath.subtract(num1, num2)} \033[0m")
        OnionMath.spacer(1)

        # Insert Solution And Type Into The List
        PastActions.append(f"Subtraction: {num1} - {num2} = " + str(OnionMath.subtract(num1, num2)))

    # Multiplication Mode
    if Mode2 == 3:

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Both Numbers To Add Together
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))

        # Run Multiply Function
        OnionMath.spacer(1)
        print(f"\033[32mSolution: {OnionMath.multiply(num1, num2)} \033[0m")
        OnionMath.spacer(1)

        # Insert Solution And Type Into The List
        PastActions.append(f"Multiplication: {num1} x {num2} = " + str(OnionMath.multiply(num1, num2)))

    # Division Mode
    if Mode2 == 4:

        # Spacer Print
        OnionMath.spacer(1)

        # Tells User To Enter Bigger Number First
        print("\033[91mNOTE: PLEASE ENTER BIGGER NUMBER FIRST THEN SMALLER NUMBER LAST \033[0m")

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Both Numbers To Subtract Together
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))

        # Run Divide Function
        OnionMath.spacer(1)
        print(f"\033[32mSolution: {OnionMath.divide(num1, num2)} \033[0m")
        OnionMath.spacer(1)

        # Insert Solution And Type Into The List
        PastActions.append(f"Division: {num1} / {num2} = " + str(OnionMath.divide(num1, num2)))

    # Exponent Mode
    if Mode2 == 5:
        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Both Numbers To Subtract Together
        num = int(input("Enter The Number: "))
        exponent = int(input("Enter the Exponent: "))

        # Run Divide Function
        OnionMath.spacer(1)
        print(f"\033[32mSolution: {OnionMath.powers(num, exponent)} \033[0m")
        OnionMath.spacer(1)

        # Insert Solution And Type Into The List
        PastActions.append(f"Powers(Exponents): {num} ** {exponent} = " + str(OnionMath.powers(num, exponent)))

    # Square Root Mode
    if Mode2 == 6:
        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Both Numbers To Subtract Together
        num = int(input("Enter The Number: "))

        # Run Divide Function
        OnionMath.spacer(1)
        print(f"\033[32mSolution: {math.sqrt(num)} \033[0m")
        OnionMath.spacer(1)

        # Insert Solution And Type Into The List
        PastActions.append(f"Square Root: {num} = " + str(math.sqrt(num)))