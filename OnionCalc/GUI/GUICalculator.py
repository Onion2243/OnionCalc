# Imports My Own Custom Created Colors Library
from Libraries.OnionColors.onioncolors import onioncolors

# Import Python Built In Math Library
import math

# Import Setup Dependencies Script
from OnionCalc.setup_script import Install_Dependency_GUI

# Runs The GUI Dependency Installer
Install_Dependency_GUI()

# Attempts To Run The GUI Code, If PySide6 Cannot Be Found Tell The User To Install It
try:
    # Import PySide6 GUI Library
    from PySide6 import QtGui, QtCore, QtWidgets
    import sys


    # The Calculator Window For OnionCalc
    class OnionCalcWindow(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
    
            self.Number1 = QtWidgets.QPushButton("1")
            self.Number2 = QtWidgets.QPushButton("2")
            self.Enter = QtWidgets.QPushButton("=")
            self.text = QtWidgets.QLabel("Calculator",alignment=QtCore.Qt.AlignCenter)
            self.sum = QtWidgets.QLabel("Calculator",alignment=QtCore.Qt.AlignCenter)
    
            self.layout = QtWidgets.QVBoxLayout(self)
            self.layout.addWidget(self.text)
            self.layout.addWidget(self.Number1)
            self.layout.addWidget(self.Number2)
            self.layout.addWidget(self.Enter)
            self.layout.addWidget(self.sum)
            
    
    def GUICalculator():
        app = QtWidgets.QApplication(sys.argv)
    
        window = OnionCalcWindow()
        window.show()
    
        app.exec()
except ModuleNotFoundError:
    print("")
    print("PySide6 Is Required to Run GUI Mode And It Is Currently Not Installed")
    print(f"Install It By Running The Command")
    print("")
    print(f"{onioncolors.text_color("green")}pip3 install PySide6 \033[0m")
    print("")
    print("Or If you'd like replace the command with any version of PySide6, JUST MAKE SURE IT IS PYSIDE6")