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
def Geomentry_Mode():
    # Print Choices

    # Go Back And Print Spacer
    OnionMath.spacer(1)
    print("0: Go Back")

    mode2 = int(input("Enter the Type Of Mode: "))

    if mode2 == 1:
        print("Hello")