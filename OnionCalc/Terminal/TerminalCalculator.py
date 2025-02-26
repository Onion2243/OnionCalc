

# Import Onion Colors Library]
from Libraries.OnionColors.onioncolors import onioncolors

# Import Python Built In Math Library
import math

# Import The Onion Calculator Functions File
from Libraries.OnionMath.functions import OnionMath

# Import Sympy And Sympy Symbols
import Libraries.SymPy as SymPy

# Past Actions List
PastActions = []

def TerminalCalculator():
    
    # Prints Out Calculator Title When The Program Starts
    print(onioncolors.text_color("orange"),"""
        ------------------------------------------------------------------------------------------------
                                        ALGEBRAIC CALCULATOR V.0.1.0
        ------------------------------------------------------------------------------------------------
        \033[0m
        """,
          )


    # Keep The Program Constantly Running Until Specified To Quit
    while True:
            # Print Choices
            print("1: Artithmatic Functions")
            print("2: Algebraic Functions")
            print("3: Geomentry")
            print("4: Triginomentry")
            print("5: Conversion")
            print("6: Quits Program")
        
            # Spacer Print
            OnionMath.spacer(2)
        
            print("0: Show Your Past Calculations")
        
            # Spacer Print
            OnionMath.spacer(1)
        
            # Try To Do This, If Given The Incorrect Value (Not An Int), Tell User Not A Valid Input And Retry
            try:
                # Ask User Which Arthimatic Mode They Want To Use
                Mode = int(input("Enter The Type Of Mode: "))
        
                # Arthimatic Functions
                if Mode == 1:
        
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
                        print(f"{onioncolors.text_color("green")}Solution: {OnionMath.add(num1, num2)} \033[0m")
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
                        print(f"{onioncolors.text_color("green")}Solution: {OnionMath.subtract(num1, num2)} \033[0m")
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
                        print(f"{onioncolors.text_color("green")}Solution: {OnionMath.multiply(num1, num2)} \033[0m")
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
                        print(f"{onioncolors.text_color("green")}Solution: {OnionMath.divide(num1, num2)} \033[0m")
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
                        print(f"{onioncolors.text_color("green")}Solution: {OnionMath.powers(num, exponent)} \033[0m")
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
                        print(f"{onioncolors.text_color("green")}Solution: {math.sqrt(num)} \033[0m")
                        OnionMath.spacer(1)
        
                        # Insert Solution And Type Into The List
                        PastActions.append(f"Square Root: {num} = " + str(math.sqrt(num)))

                # Algebraic Mode
                if Mode == 2:
                    # Spacer Print
                    OnionMath.spacer(1)
        
                    # List Of Algebraic Functions
                    print("1: Basic Algebra")
                    print("2: Systems Of Equations")
                    print("3: Equation To Slope Intercept Form")
                    print("4: Functions")

                    OnionMath.spacer(1)
                    print("Algebra Based Conversions")
                    print("20: Log(Logarithm)")

                    # Go Back And Print Spacer
                    OnionMath.spacer(1)
                    print("0: Go Back")

                    # Spacer Print
                    OnionMath.spacer(1)
        
                    # Ask User Which Mode They Use
                    Mode2 = int(input("Enter the Type Of Mode: "))
        
                    # Basic Algebra
                    if Mode2 == 1:
                        # Spacer Print Statement
                        OnionMath.spacer(1)
        
                        # Set SymPy Variable X
                        x = SymPy.Symbol("x")
        
                        # Ask User The Left And Right Side Of The Equation
                        left_side_equation1 = input("Enter The Left Side Of The Equation (Note: Please Use X Only): ")
                        right_side_equation1 = input("Enter The Right Side Of The Equation (Note: Please Use X Only): ")
        
                        # Convert Input Into A Sympy Expression
                        left_side_expression = SymPy.sympify(left_side_equation1)
                        right_side_expression = SymPy.sympify(right_side_equation1)
        
                        # Create An Equation Out Of SymPy
                        equation = SymPy.Eq(left_side_expression, right_side_expression)
        
                        OnionMath.spacer(1)
                        # Solve And Print The Equation
                        solution = SymPy.solve(equation, x)
                        print("\033[92mSolution: ",solution,"\033[0m")
                        OnionMath.spacer(1)
        
                        # Insert Solution And Type Into The List
                        PastActions.append(f"Basic Algebra: {left_side_expression} = {right_side_expression} x = " + str(solution))
        
                    # Systems Of Equations
                    if Mode2 == 2:
                        # Spacer Print Statement
                        OnionMath.spacer(1)
        
                        # Ask User The Left And Right Side Of Equation 1 And 2
                        left_side_expression1 = input("Enter The Left Side Of The First Equation (Note: Please Use X And Y Only): ")
                        right_side_expression1 = input("Enter The Right Side Of The First Equation (Note: Please Use X And Y Only): ")
        
                        left_side_expression2 = input("Enter The Left Side Of The Second Equation (Note: Please Use X And Y Only): ")
                        right_side_expression2 = input("Enter The Right Side Of The Second Equation (Note: Please Use X And Y Only): ")
        
                        # Convert Both Equations Into A Sympy Equation
                        left_side_equation1 = SymPy.sympify(left_side_expression1)
                        right_side_equation1 = SymPy.sympify(right_side_expression1)
                        left_side_equation2 = SymPy.sympify(left_side_expression2)
                        right_side_equation2 = SymPy.sympify(right_side_expression2)
        
                        # Create An Equation Out Of SymPy
                        equation1 = SymPy.Eq(left_side_equation1, right_side_equation1)
                        equation2 = SymPy.Eq(left_side_equation2, right_side_equation2)
                        # Spacer Print
        
                        OnionMath.spacer(1)
        
                        # Solve And Print The Equation
                        solution = SymPy.solve([equation1, equation2],  [x, y])
                        a = print("\033[92mSolution: ",solution,"\033[0m")
                        OnionMath.spacer(1)
        
                        # Insert Solution And Type Into The List
                        PastActions.append(f"Systems Of Equations: [{left_side_equation1} = {right_side_equation1}] , [{left_side_equation2} = {right_side_equation2}] " + str(solution))

                    # Equation To Slope Intercept Form
                    if Mode2 == 3:
                        # Spacer Print Statement
                        OnionMath.spacer(1)
        
                        x, y = SymPy.symbols("x y")
        
                        # Ask User The Left And Right Side Of The Equation
                        left_side_equation1 = input("Enter The Left Side Of The Equation (Note: Please Use X Only): ")
                        right_side_equation1 = input("Enter The Right Side Of The Equation (Note: Please Use X Only): ")
        
                        # Convert Input Into A Sympy Expression
                        left_side_expression = SymPy.sympify(left_side_equation1)
                        right_side_expression = SymPy.sympify(right_side_equation1)
        
                        # Create An Equation Out Of SymPy
                        equation = SymPy.Eq(left_side_expression, right_side_expression)
        
                        OnionMath.spacer(1)
                        # Solve And Print The Slope Intercept Form
                        solution = SymPy.solve(equation, y)[0] # Solves The Equation And Attempts To Get Y = 0
                        solution2 = SymPy.solve(equation, x)[0] # Solves The Equation And Attempts To Get X = 0
                        print(f"\033[92mSolution: y =",solution,"\033[0m")
                        print(f"\033[92mSolution: x =",solution2,"\033[0m")
                        OnionMath.spacer(1)
        
                        PastActions.append(f"Equation To Slope Intercept Form: {left_side_expression} = {right_side_expression} → y =" + str(solution))

                    # Functions
                    if Mode2 == 4:
                        # Spacer Print Statement
                        OnionMath.spacer(1)

                        # Define All The Variables
                        x = SymPy.Symbol("x")

                        # Create A SymPy Function
                        function = SymPy.Function('F')(x)

                        # Allows The User To Enter The Function Plug In Value
                        function = input("Enter The Function: F(")

                        # Asks The User The Expression
                        expression = input("Enter The Expression: ")

                        # Convert Input Into A Sympy Expression
                        expression = SymPy.sympify(expression)

                        # Makes The Solution By Subbing In The Function Value To X
                        solution = expression.subs(x, function)

                        # Prints The Solution
                        OnionMath.spacer(1)
                        print(f"\033[92mSolution: ", solution, "\033[0m")
                        OnionMath.spacer(1)

                        # Adds The Function To The Past Actions List
                        PastActions.append(f"Function: F({function}) = {expression} = " + str(solution))
        
                    # Logarithm
                    if Mode2 == 20:
                        # Spacer Print
                        OnionMath.spacer(1)
        
                        # List Of Algebraic Functions
                        print("1: Log")
                        print("2: Log 2")
                        print("3: Log 10")
        
                        # Spacer Print
                        OnionMath.spacer(1)
        
                        # Ask User Which Mode They Use
                        Mode3 = int(input("Enter the Type Of Mode: "))
        
                        # Log Mode
                        if Mode3 == 1:
                            base = float(input("Enter The Base Of Log: "))
                            num = float(input("Enter The Number You Want To Get The Log Of: "))
        
                            # Get And Print The Sine Of The Inputted Number
                            OnionMath.spacer(1)
                            print("\033[92mSolution: ",math.log(num, base),"\033[0m")
                            OnionMath.spacer(1)
        
                            # Insert Solution And Type Into The List
                            PastActions.append(f"Log(Base {base}): {num} =  " + str(math.log(num, base)))
        
                        # Log With Base 2
                        if Mode3 == 2:
                            num = float(input("Enter The Number You Want To Get The Log(Base 2) Of: "))
        
                            # Get And Print The Sine Of The Inputted Number
                            OnionMath.spacer(1)
                            print("\033[92mSolution: ",math.log2(num),"\033[0m")
                            OnionMath.spacer(1)
        
                            # Insert Solution And Type Into The List
                            PastActions.append(f"Log(Base 2): {num} =  " + str(math.log2(num)))
        
                        # Log With Base 10
                        if Mode3 == 2:
                            num = float(input("Enter The Number You Want To Get The Log(Base 10) Of: "))
        
                            # Get And Print The Sine Of The Inputted Number
                            OnionMath.spacer(1)
                            print("\033[92mSolution: ",math.log10(num),"\033[0m")
                            OnionMath.spacer(1)
        
                            # Insert Solution And Type Into The List
                            PastActions.append(f"Log(Base 10): {num} =  " + str(math.log10(num)))
        
                # Geomentry Mode        
                if Mode == 3:
                    # Print Choices

                    # Go Back And Print Spacer
                    OnionMath.spacer(1)
                    print("0: Go Back")
        
                    mode2 = int(input("Enter the Type Of Mode: "))
        
                    if mode2 == 1:
                        print("Hello")
        
                # Triginomentry Mode     
                if Mode == 4:
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
        
                # Conversion Mode
                if Mode == 5:
                    # Print Choices And Spacer Print
                    OnionMath.spacer(1)
                    print("1: Fraction To Decimal")
                    print("2: Decimal To Fraction")
                    print("3: Percentages")
                    OnionMath.spacer(1)

                    # Go Back And Print Spacer
                    OnionMath.spacer(1)
                    print("0: Go Back")
        
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

                # Quits The Program If Prompted  
                if Mode == 6:

                    # Print Thank You Message
                    OnionMath.thank_you_message()
        
                    # End The Program By Breaking From The While Loop
                    break
        
                # Prints Out Past Calculations
                if Mode == 0:
                    OnionMath.spacer(1)
                    print("\033[92mPast Calculations: " + str(PastActions) + "\033[0m")
                    OnionMath.spacer(1)
        
            except ValueError:
                OnionMath.spacer(1)
                print("\033[31mNOT A VALID INPUT, TRY AGAIN\033[0m")
                OnionMath.spacer(1)
            except KeyboardInterrupt:
                # Print Thank You Message, Number Is Included In Order To Bypass An Error With Self
                OnionMath.thank_you_message(1)
        
                break