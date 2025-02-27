import subprocess
import sys
import os

def Install_Dependency_Terminal():
    try:
        # Attempt To Import System
        import sympy
    except ImportError:
        print("Required dependencies not found. Installing now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "sympy"], check=True)

def Install_Dependency_GUI():
    try:
        # Attempts To Import PySide6 And Sympy
        import PySide6
        import sympy
    except ImportError:
        print("Required dependencies not found. Installing now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "sympy"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "PySide6"], check=True)
        
def Uninstall_Dependency_And_OnionCalc():
    print("ARE YOU SURE YOU WANT TO UNINSTALL ONIONCALC")
    double_check = input("Do you want to uninstall ONIONCALC? (y/n) ")
    
    if double_check == "y":
        print("Uninstalling OnionCalc")
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "sympy"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "PySide6"], check=True)
        os.remove("../../")
    
        

