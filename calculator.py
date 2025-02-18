"""
    Below Is The Algebra 1 Calculator, Currently It Has 4 Major Functions
    
    1. Basic Arthmatic
    2. Algebraic Equations, (Linear)
    3. Conversions
    4. Other Advanced Math Functions (Sin, Cosin, And Tangent)

    In Order To Use This Calculator You Will Need To Have Python 3.14 Installed, If you want to read or edit
    the code look below this comment
    
    
"""

"""
    LIST OF LIBRARIES:
        - Python Math Library
        - SymPy (Symbolic Mathematics Library)
        - Python Function Library
        - OnionColors (My Text And Background Color Library)
"""

# Imports My Own Custom Created Colors Library
import onioncolors

# Import Python Built In Math Library
import math

# Import Sympy And Sympy Symbols
import sympy as SymPy
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

# Import Python Built In Fraction Library
from fractions import Fraction

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

# Past Actions List
PastActions = []

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
    print("""
    """)
    
    print("0: Show Your Past Calculations")
    
    # Spacer Print
    print("")
    
    # Try To Do This, If Given The Incorrect Value (Not An Int), Tell User Not A Valid Input And Retry
    try:
        # Ask User Which Arthimatic Mode They Want To Use
        Mode = int(input("Enter The Type Of Mode: "))

        # Arthimatic Functions
        if Mode == 1:
            
            # Spacer Print
            print("")
            
            # Print Choices
            print("1: Addition")
            print("2: Subtraction")
            print("3: Multiplication")
            print("4: Division")
            print("5: Exponents")
            
            # Spacer Print
            print("")
            
            Mode2 = int(input("Enter The Type Of Mode: "))
            
            # Spacer Print
            print("")
    
            # Addition Mode
            if Mode2 == 1:
                
                # Spacer Print
                print("")
                
                # Ask User Both Numbers To Add Together
                num1 = int(input("Enter the First Number: "))
                num2 = int(input("Enter the Second Number: "))
                
                # Run Add Function
                print("")
                print(f"{onioncolors.text_color("green")}Solution: {add(num1, num2)} \033[0m")
                print("")
    
                # Insert Solution And Type Into The List
                PastActions.append(f"Addition: {num1} + {num2} = " + str(add(num1, num2)))
        
            # Subtraction Mode
            if Mode2 == 2:
    
                # Spacer Print
                print("")
        
                # Tells User To Enter Bigger Number First
                print("\033[91mNOTE: PLEASE ENTER BIGGER NUMBER FIRST THEN SMALLER NUMBER LAST \033[0m")
    
                # Spacer Print
                print("")
        
                # Ask User Both Numbers To Subtract Together
                num1 = int(input("Enter the First Number: "))
                num2 = int(input("Enter the Second Number: "))
        
                # Run Subtraction Function
                print("")
                print(f"{onioncolors.text_color("green")}Solution: {subtract(num1, num2)} \033[0m")
                print("")
                
                # Insert Solution And Type Into The List
                PastActions.append(f"Subtraction: {num1} - {num2} = " + str(subtract(num1, num2)))
        
            # Multiplication Mode
            if Mode2 == 3:
    
                # Spacer Print
                print("")
        
                # Ask User Both Numbers To Add Together
                num1 = int(input("Enter the First Number: "))
                num2 = int(input("Enter the Second Number: "))
        
                # Run Multiply Function
                print("")
                print(f"{onioncolors.text_color("green")}Solution: {multiply(num1, num2)} \033[0m")
                print("")
    
                # Insert Solution And Type Into The List
                PastActions.append(f"Multiplication: {num1} x {num2} = " + str(multiply(num1, num2)))
                
            # Division Mode
            if Mode2 == 4:
    
                # Spacer Print
                print("")
        
                # Tells User To Enter Bigger Number First
                print("\033[91mNOTE: PLEASE ENTER BIGGER NUMBER FIRST THEN SMALLER NUMBER LAST \033[0m")
    
                # Spacer Print
                print("")
        
                # Ask User Both Numbers To Subtract Together
                num1 = int(input("Enter the First Number: "))
                num2 = int(input("Enter the Second Number: "))
        
                # Run Divide Function
                print("")
                print(f"{onioncolors.text_color("green")}Solution: {divide(num1, num2)} \033[0m")
                print("")
    
                # Insert Solution And Type Into The List
                PastActions.append(f"Division: {num1} / {num2} = " + str(divide(num1, num2)))
                
            # Exponent Mode
            if Mode2 == 5:
                # Spacer Print
                print("")

                # Ask User Both Numbers To Subtract Together
                num = int(input("Enter The Number: "))
                exponent = int(input("Enter the Exponent: "))

                # Run Divide Function
                print("")
                print(f"{onioncolors.text_color("green")}Solution: {powers(num, exponent)} \033[0m")
                print("")

                # Insert Solution And Type Into The List
                PastActions.append(f"Powers(Exponents): {num} ** {exponent} = " + str(powers(num, exponent)))
                
            
        # Algebraic Mode
        if Mode == 2:
            # Spacer Print
            print("")
            
            # List Of Algebraic Functions
            print("1: Basic Algebra")
            print("2: Systems Of Equations")
            print("3: Equation To Slope Intercept Form")
            
            print("20: Log(Logarithm)")
            
            
            # Spacer Print
            print("")
            
            # Ask User Which Mode They Use
            Mode2 = int(input("Enter the Type Of Mode: "))
    
            # Basic Algebra
            if Mode2 == 1:
                # Spacer Print Statement
                print("")
    
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
    
                print("")
                # Solve And Print The Equation
                solution = SymPy.solve(equation, x)
                print("\033[92mSolution: ",solution,"\033[0m")
                print()
                
                # Insert Solution And Type Into The List
                PastActions.append(f"Basic Algebra: {left_side_expression} = {right_side_expression} x = " + str(solution))
            
            # Systems Of Equations
            if Mode2 == 2:
                # Spacer Print Statement
                print("")
            
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
                
                print("")
                
                # Solve And Print The Equation
                solution = SymPy.solve([equation1, equation2],  [x, y])
                a = print("\033[92mSolution: ",solution,"\033[0m")
                print()
    
                # Insert Solution And Type Into The List
                PastActions.append(f"Systems Of Equations: [{left_side_equation1} = {right_side_equation1}] , [{left_side_equation2} = {right_side_equation2}] " + str(solution))
                
            if Mode2 == 3:
                # Spacer Print Statement
                print("")
                
                x, y = SymPy.symbols("x y")

                # Ask User The Left And Right Side Of The Equation
                left_side_equation1 = input("Enter The Left Side Of The Equation (Note: Please Use X Only): ")
                right_side_equation1 = input("Enter The Right Side Of The Equation (Note: Please Use X Only): ")

                # Convert Input Into A Sympy Expression
                left_side_expression = SymPy.sympify(left_side_equation1)
                right_side_expression = SymPy.sympify(right_side_equation1)

                # Create An Equation Out Of SymPy
                equation = SymPy.Eq(left_side_expression, right_side_expression)

                print("")
                # Solve And Print The Slope Intercept Form
                solution = SymPy.solve(equation, y)[0] # Solves The Equation And Attempts To Get Y = 0
                solution2 = SymPy.solve(equation, x)[0] # Solves The Equation And Attempts To Get X = 0
                print(f"\033[92mSolution: y =",solution,"\033[0m")
                print(f"\033[92mSolution: x =",solution2,"\033[0m")
                print()

                PastActions.append(f"Equation To Slope Intercept Form: {left_side_expression} = {right_side_expression} → y =" + str(solution))
                
                
            # Logarithm
            if Mode2 == 20:
                # Spacer Print
                print("")
    
                # List Of Algebraic Functions
                print("1: Log")
                print("2: Log 2")
                print("3: Log 10")
    
                # Spacer Print
                print("")
    
                # Ask User Which Mode They Use
                Mode3 = int(input("Enter the Type Of Mode: "))
                
                # Log Mode
                if Mode3 == 1:
                    base = float(input("Enter The Base Of Log: "))
                    num = float(input("Enter The Number You Want To Get The Log Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.log(num, base),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Log(Base {base}): {num} =  " + str(math.log(num, base)))
                
                # Log With Base 2
                if Mode3 == 2:
                    num = float(input("Enter The Number You Want To Get The Log(Base 2) Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.log2(num),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Log(Base 2): {num} =  " + str(math.log2(num)))

                # Log With Base 10
                if Mode3 == 2:
                    num = float(input("Enter The Number You Want To Get The Log(Base 10) Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.log10(num),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Log(Base 10): {num} =  " + str(math.log10(num)))
                    
        # Geomentry Mode        
        if Mode == 3:
            # Print Choices
        
            mode2 = int(input("Enter the Type Of Mode: "))
            
            if mode2 == 1:
                print("Hello")
            
        # Triginomentry Mode     
        if Mode == 4:
            # Spacer Print
            print("")
            
            # Print Choices
            print("1: Sin")
            print("2: Cos")
            print("3: Tan")
    
            # Spacer Print
            print("")
            
            # Ask User Type Of Mode
            Mode2 = int(input("Enter the Type Of Mode: "))
            
            # Sin Choices
            if Mode2 == 1:
    
                # Spacer Print
                print("")
                
                # Print Choices
                print("1: Sin")
                print("2: Hyperbolic Sin")
                print("3: Arc Sin")
                print("4: Inverse Hyperbolic Sin")
    
                # Spacer Print
                print("")
                
                # Ask User Type Of Mode
                Mode3 = int(input("Enter the Type Of Mode: "))
                
                # Sin
                if Mode3 == 1:
                
                    num = float(input("Enter the Number You Want To Get The Sine Of: "))
                    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.sin(num),"\033[0m")
                    print("")
        
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Sine: {num} → " + str(math.sin(num)))
    
                # Hyperbolic Sin
                if Mode3 == 2:
    
                    num = float(input("Enter the Number You Want To Get The Hyperbolic Sine Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.sinh(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Hyperbolic Sine: {num} → " + str(math.sinh(num)))
    
                # Arc Sin
                if Mode3 == 3:
    
                    num = float(input("Enter the Number You Want To Get The Arc Sine Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.asin(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Arc Sine: {num} → " + str(math.asin(num)))
    
                # Inverse Hyperbolic Sin
                if Mode3 == 4:
    
                    num = float(input("Enter the Number You Want To Get The Inverse Hyperbolic Sine Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.asinh(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Inverse Hyperbolic Sine: {num} → " + str(math.asinh(num)))
    
            # Cos Choices
            if Mode2 == 2:
    
                # Spacer Print
                print("")
    
                # Print Choices
                print("1: Cos")
                print("2: Hyperbolic Cos")
                print("3: Arc Cos")
                print("4: Inverse Hyperbolic Cos")
    
                # Spacer Print
                print("")
    
                # Ask User Type Of Mode
                Mode3 = int(input("Enter the Type Of Mode: "))
    
                # Cos
                if Mode3 == 1:
    
                    num = float(input("Enter the Number You Want To Get The Cos Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.cos(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Cos: {num} → " + str(math.cos(num)))
    
                # Hyperbolic Cos
                if Mode3 == 2:
    
                    num = float(input("Enter the Number You Want To Get The Hyperbolic Cos Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.cosh(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Hyperbolic Cos: {num} → " + str(math.cosh(num)))
    
                # Arc Cos
                if Mode3 == 3:
    
                    num = float(input("Enter the Number You Want To Get The Arc Cos Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.acos(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Arc Cos: {num} → " + str(math.acos(num)))
    
                # Inverse Hyperbolic Cos
                if Mode3 == 4:
    
                    num = float(input("Enter the Number You Want To Get The Inverse Hyperbolic Cos Of: "))
    
                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.acosh(num),"\033[0m")
                    print("")
    
                    # Insert Solution And Type Into The List
                    PastActions.append(f"Inverse Hyperbolic Cos: {num} → " + str(math.acosh(num)))

            # Tan Choices
            if Mode2 == 3:

                # Spacer Print
                print("")

                # Print Choices
                print("1: Tan")
                print("2: Hyperbolic Tan")
                print("3: Arc Tan")
                print("4: Inverse Hyperbolic Tan")

                # Spacer Print
                print("")

                # Ask User Type Of Mode
                Mode3 = int(input("Enter the Type Of Mode: "))

                # Tan
                if Mode3 == 1:

                    num = float(input("Enter the Number You Want To Get The Tan Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.tan(num),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Tan: {num} → " + str(math.tan(num)))

                # Hyperbolic Tan
                if Mode3 == 2:

                    num = float(input("Enter the Number You Want To Get The Hyperbolic Tan Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.tanh(num),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Hyperbolic Tan: {num} → " + str(math.tanh(num)))

                # Arc Tan
                if Mode3 == 3:

                    num = float(input("Enter the Number You Want To Get The Arc Tan Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.atan(num),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Arc Tan: {num} → " + str(math.atan(num)))

                # Inverse Hyperbolic Tan
                if Mode3 == 4:

                    num = float(input("Enter the Number You Want To Get The Inverse Hyperbolic Tan Of: "))

                    # Get And Print The Sine Of The Inputted Number
                    print("")
                    print("\033[92mSolution: ",math.atanh(num),"\033[0m")
                    print("")

                    # Insert Solution And Type Into The List
                    PastActions.append(f"Inverse Hyperbolic Tan: {num} → " + str(math.atanh(num)))
    
        # Conversion Mode
        if Mode == 5:
            # Print Choices And Spacer Print
            print("1: Fraction To Decimal")
            print("2: Decimal To Fraction")
            print("")
    
            # Ask User Which Mode They Want
            mode2 = int(input("Enter the Type Of Mode: "))
    
            # Fraction To Decimal Mode
            if mode2 == 1:
                numerator = int(input("Enter the Numerator (Top Number) Of The Fraction: "))
                denominator = int(input("Enter the Denominator (Bottom Number) Of The Fraction: "))
                print("")
                print("\033[92mSolution: ",fraction_to_decimal(numerator, denominator),"\033[0m")
                print("")
                PastActions.append(f"Fraction To Decimal: {numerator}/{denominator} → " + str(fraction_to_decimal(numerator, denominator)))
    
            # Decimal To Fraction Mode
            if mode2 == 2:
                decimal = float(input("Enter the Decimal You Want to Convert: "))
    
                print("")
                print("\033[92mSolution: ",decimal_to_fraction(decimal),"\033[0m")
                print("")
    
                # Add The Decimal To Fraction Into The Past Calculations List
                PastActions.append(f"Fraction To Decimal: {decimal} → " + str(decimal_to_fraction(decimal)))
                    
        # Quits The Program If Prompted  
        if Mode == 6:
            
            # Prints Thanks For Using Message
            print("""
            
    Thank You For Using
            
    ------------------------------------------------------------------------------------------------
                                            ALGEBRAIC CALCULATOR V.0.1.0
    ------------------------------------------------------------------------------------------------
    """)
            
            # End The Program By Breaking From The While Loop
            break
        
        # Prints Out Past Calculations
        if Mode == 0:
            print("")
            print("\033[92mPast Calculations: " + str(PastActions) + "\033[0m")
            print("")
    except ValueError:
        print("")
        print("\033[31mNOT A VALID INPUT, TRY AGAIN\033[0m")
        print("")
    except KeyboardInterrupt:
        # Prints Thanks For Using Message
        print("""
            
    Thank You For Using
            
    ------------------------------------------------------------------------------------------------
                                            ALGEBRAIC CALCULATOR V.0.1.0
    ------------------------------------------------------------------------------------------------
    """)

        break
        