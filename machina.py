#! /usr/bin/env python
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from app.mainapp import mainwindow

def main():
    qapp = QApplication(sys.argv)
    win = QMainWindow()
    gui = mainwindow.Ui_MainWindow()
    gui.setupUi(win)
    win.show()
    sys.exit(qapp.exec_())

if __name__ == '__main__':
    main()
