# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:39:27 2024

@author: megan
"""

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from hmwk10Python7 import Ui_Dialog  

class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)

      
        self.pushButton_4.clicked.connect(self.close_application)

        self.m = None
        self.c = None
        self.k = None

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphicsLayout = QVBoxLayout(self.graphicsView_PIDControlGraph)
        self.graphicsLayout.addWidget(self.canvas)

    def close_application(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
