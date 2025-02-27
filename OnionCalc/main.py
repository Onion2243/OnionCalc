"""
    LIST OF LIBRARIES/Credits:
        - Python Math Library
        - SymPy (Symbolic Mathematics Library)
        - Python Fractions Library
        - OnionColors (My Text And Background Color Library)
"""

# Imports The GUI And Terminal Based Calculators
from Terminal.TerminalCalculator import TerminalCalculator
from GUI.GUICalculator import GUICalculator

# Import The Dependency Checker
from setup_script import Install_Dependency_Terminal

# Runs The Dependency Checker
Install_Dependency_Terminal()

# Print Options
print("")
print("1: Terminal")
print("2: GUI")
print("""
""")
print("0: Uninstall OnionCalc And Its Dependencies")

# Allows User To Select GUI Or Terminal Based Calculator
SelectType = int(input("Please Enter The Mode: "))

try: 
    if SelectType == 1:
        TerminalCalculator()
    elif SelectType == 2:
        GUICalculator()
    else:
        print("Not A Valid Input")
except KeyboardInterrupt:
    print("User Interrupted, Exiting OnionCalc")
    