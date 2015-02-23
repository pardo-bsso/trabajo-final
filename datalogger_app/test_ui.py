#!/usr/bin/env python

import main_ui

import sys

from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    win = QtGui.QMainWindow()
    ui = main_ui.Ui_MainWindow()
    ui.setupUi(win)

    win.show()

    sys.exit(app.exec_())
