# Imports My Own Custom Created Colors Library
import onioncolors

# Import Python Built In Math Library
import math

# Import Sympy And Sympy Symbols
import sympy as SymPy
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

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