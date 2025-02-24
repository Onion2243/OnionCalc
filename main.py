"""
    LIST OF LIBRARIES/Credits:
        - Python Math Library
        - SymPy (Symbolic Mathematics Library)
        - Python Fractions Library
        - OnionColors (My Text And Background Color Library)
"""

# Imports The GUI And Terminal Based Calculators
from Files.TerminalCalculator import TerminalCalculator
from Files.GUICalculator import GUICalculator

# Print Options
print("")
print("1: Terminal")
print("2: GUI")
print("")

# Allows User To Select GUI Or Terminal Based Calculator
SelectType = int(input("Please Enter The Mode: "))
        
if SelectType == 1:
    TerminalCalculator()
elif SelectType == 2:
    GUICalculator()
else:
    print("Not A Valid Input")
    