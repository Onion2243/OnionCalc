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

def Triginomentry_Mode():

    print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Opening Trigonometry Calculator
------------------------------------------------------------------------------------------------
\033[0m
""",)
    
    # Spacer Print
    OnionMath.spacer(1)

    # Print Choices
    print("1: Sin")
    print("2: Cos")
    print("3: Tan")

    # Go Back And Print Spacer
    OnionMath.spacer(1)
    print("0: Go Back")

    # Spacer Print
    OnionMath.spacer(1)

    # Ask User Type Of Mode
    Mode2 = int(input("Enter the Type Of Mode: "))

    # Sin Choices
    if Mode2 == 1:

        # Spacer Print
        OnionMath.spacer(1)

        # Print Choices
        print("1: Sin")
        print("2: Hyperbolic Sin")
        print("3: Arc Sin")
        print("4: Inverse Hyperbolic Sin")

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Type Of Mode
        Mode3 = int(input("Enter the Type Of Mode: "))

        # Sin
        if Mode3 == 1:

            num = float(input("Enter the Number You Want To Get The Sine Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.sin(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Sine: {num} → " + str(math.sin(num)))

        # Hyperbolic Sin
        if Mode3 == 2:

            num = float(input("Enter the Number You Want To Get The Hyperbolic Sine Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.sinh(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Hyperbolic Sine: {num} → " + str(math.sinh(num)))

        # Arc Sin
        if Mode3 == 3:

            num = float(input("Enter the Number You Want To Get The Arc Sine Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.asin(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Arc Sine: {num} → " + str(math.asin(num)))

        # Inverse Hyperbolic Sin
        if Mode3 == 4:

            num = float(input("Enter the Number You Want To Get The Inverse Hyperbolic Sine Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.asinh(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Inverse Hyperbolic Sine: {num} → " + str(math.asinh(num)))

    # Cos Choices
    if Mode2 == 2:

        # Spacer Print
        OnionMath.spacer(1)

        # Print Choices
        print("1: Cos")
        print("2: Hyperbolic Cos")
        print("3: Arc Cos")
        print("4: Inverse Hyperbolic Cos")

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Type Of Mode
        Mode3 = int(input("Enter the Type Of Mode: "))

        # Cos
        if Mode3 == 1:

            num = float(input("Enter the Number You Want To Get The Cos Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.cos(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Cos: {num} → " + str(math.cos(num)))

        # Hyperbolic Cos
        if Mode3 == 2:

            num = float(input("Enter the Number You Want To Get The Hyperbolic Cos Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.cosh(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Hyperbolic Cos: {num} → " + str(math.cosh(num)))

        # Arc Cos
        if Mode3 == 3:

            num = float(input("Enter the Number You Want To Get The Arc Cos Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.acos(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Arc Cos: {num} → " + str(math.acos(num)))

        # Inverse Hyperbolic Cos
        if Mode3 == 4:

            num = float(input("Enter the Number You Want To Get The Inverse Hyperbolic Cos Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.acosh(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Inverse Hyperbolic Cos: {num} → " + str(math.acosh(num)))

    # Tan Choices
    if Mode2 == 3:

        # Spacer Print
        OnionMath.spacer(1)

        # Print Choices
        print("1: Tan")
        print("2: Hyperbolic Tan")
        print("3: Arc Tan")
        print("4: Inverse Hyperbolic Tan")

        # Spacer Print
        OnionMath.spacer(1)

        # Ask User Type Of Mode
        Mode3 = int(input("Enter the Type Of Mode: "))

        # Tan
        if Mode3 == 1:

            num = float(input("Enter the Number You Want To Get The Tan Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.tan(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Tan: {num} → " + str(math.tan(num)))

        # Hyperbolic Tan
        if Mode3 == 2:

            num = float(input("Enter the Number You Want To Get The Hyperbolic Tan Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.tanh(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Hyperbolic Tan: {num} → " + str(math.tanh(num)))

        # Arc Tan
        if Mode3 == 3:

            num = float(input("Enter the Number You Want To Get The Arc Tan Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.atan(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Arc Tan: {num} → " + str(math.atan(num)))

        # Inverse Hyperbolic Tan
        if Mode3 == 4:

            num = float(input("Enter the Number You Want To Get The Inverse Hyperbolic Tan Of: "))

            # Get And Print The Sine Of The Inputted Number
            OnionMath.spacer(1)
            print("\033[92mSolution: ",math.atanh(num),"\033[0m")
            OnionMath.spacer(1)

            # Insert Solution And Type Into The List
            PastActions.append(f"Inverse Hyperbolic Tan: {num} → " + str(math.atanh(num)))