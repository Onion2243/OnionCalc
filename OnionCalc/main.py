"""
    LIST OF LIBRARIES/Credits:
        - Python Math Library
        - SymPy (Symbolic Mathematics Library)
        - Python Fractions Library
        - OnionColors (My Text And Background Color Library)
        
        - NOTE: I Only have knowledge with what is in this calculator, im not sure how to do calculus in
                Sympy, Only Features that are in this program, Same with any other library that i did not
                create
"""
# Imports The GUI And Terminal Based Calculators
from Terminal.TerminalCalculator import TerminalCalculator
from GUI.GUICalculator import GUICalculator

# Import The Dependency Checker
from setup_script import Install_Dependency_Terminal
from setup_script import Uninstall_Dependency_And_OnionCalc

from settings import Settings_Editor

import json

# Opens The Settings File
file = open("settings.json", "r")

def load_setting_mode_visibility():
    settings_mode_visibilty = file.readline()
    settings_mode_visibilty = json.loads(settings_mode_visibilty)
    return settings_mode_visibilty

setting_1 = load_setting_mode_visibility()

# Runs The Dependency Checker
Install_Dependency_Terminal()

print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                        Welcome To OnionCalc V.0.2.0. Please Choose A Mode
------------------------------------------------------------------------------------------------
\033[0m
""",)

# Print Options
print("")
print("1: Terminal")
print("2: GUI")
print("3: Edit Calculator Settings")
print("""
""")
print("0: Uninstall OnionCalc And Its Dependencies ")

# Allows User To Select GUI Or Terminal Based Calculator
SelectType = int(input("Please Enter The Mode: "))
    

def Run_Calculator():
    try: 
        if SelectType == 1:
            TerminalCalculator(setting_1)
        elif SelectType == 2:
            GUICalculator()
        elif SelectType == 3:
            Settings_Editor()
        elif SelectType == 0:
            Uninstall_Dependency_And_OnionCalc()
        else:
            print("Not A Valid Input")
    except KeyboardInterrupt:
        print("User Interrupted, Exiting OnionCalc")
 
Run_Calculator()
    