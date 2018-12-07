# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QMainWindow
from Ui_pyqt_Matplotlib_Widget import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.widget.setVisible(False)#静态
        self.widget_2.setVisible(False)#动态
        
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        显示静态图
        """
        self.widget.setVisible(True)
        self.widget.mpl.start_static_plot()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
       显示动态图
        """
        self.widget_2.setVisible(True)
        self.widget_2.mpl.start_dynamic_plot()
        
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
