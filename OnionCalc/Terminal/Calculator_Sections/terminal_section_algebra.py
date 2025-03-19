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



def Algebraic_Mode():

    print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Opening Algebraic Calculator
------------------------------------------------------------------------------------------------
\033[0m
""",)
    
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
        