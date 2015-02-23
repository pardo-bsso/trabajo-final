# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Sun Feb 22 18:52:56 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(828, 665)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.qwtPlot = QwtPlot(self.centralwidget)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.verticalLayout.addWidget(self.qwtPlot)
        self.xScroll = QtGui.QScrollBar(self.centralwidget)
        self.xScroll.setMinimum(60)
        self.xScroll.setMaximum(60)
        self.xScroll.setPageStep(30)
        self.xScroll.setOrientation(QtCore.Qt.Horizontal)
        self.xScroll.setObjectName(_fromUtf8("xScroll"))
        self.verticalLayout.addWidget(self.xScroll)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblZoom = QtGui.QLabel(self.centralwidget)
        self.lblZoom.setText(_fromUtf8(""))
        self.lblZoom.setObjectName(_fromUtf8("lblZoom"))
        self.horizontalLayout_2.addWidget(self.lblZoom)
        self.scWinLength = QtGui.QSlider(self.centralwidget)
        self.scWinLength.setMinimum(10)
        self.scWinLength.setMaximum(600)
        self.scWinLength.setSingleStep(10)
        self.scWinLength.setPageStep(60)
        self.scWinLength.setProperty("value", 30)
        self.scWinLength.setOrientation(QtCore.Qt.Horizontal)
        self.scWinLength.setInvertedAppearance(False)
        self.scWinLength.setInvertedControls(False)
        self.scWinLength.setObjectName(_fromUtf8("scWinLength"))
        self.horizontalLayout_2.addWidget(self.scWinLength)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cCursor1 = QtGui.QCheckBox(self.centralwidget)
        self.cCursor1.setObjectName(_fromUtf8("cCursor1"))
        self.horizontalLayout_3.addWidget(self.cCursor1)
        self.sCursor1 = QtGui.QSlider(self.centralwidget)
        self.sCursor1.setMaximum(1000)
        self.sCursor1.setProperty("value", 325)
        self.sCursor1.setOrientation(QtCore.Qt.Horizontal)
        self.sCursor1.setObjectName(_fromUtf8("sCursor1"))
        self.horizontalLayout_3.addWidget(self.sCursor1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cCursor2 = QtGui.QCheckBox(self.centralwidget)
        self.cCursor2.setObjectName(_fromUtf8("cCursor2"))
        self.horizontalLayout_4.addWidget(self.cCursor2)
        self.sCursor2 = QtGui.QSlider(self.centralwidget)
        self.sCursor2.setMaximum(1000)
        self.sCursor2.setProperty("value", 625)
        self.sCursor2.setOrientation(QtCore.Qt.Horizontal)
        self.sCursor2.setObjectName(_fromUtf8("sCursor2"))
        self.horizontalLayout_4.addWidget(self.sCursor2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bStart = QtGui.QPushButton(self.centralwidget)
        self.bStart.setObjectName(_fromUtf8("bStart"))
        self.horizontalLayout.addWidget(self.bStart)
        self.bPause = QtGui.QPushButton(self.centralwidget)
        self.bPause.setCheckable(True)
        self.bPause.setObjectName(_fromUtf8("bPause"))
        self.horizontalLayout.addWidget(self.bPause)
        self.bStop = QtGui.QPushButton(self.centralwidget)
        self.bStop.setObjectName(_fromUtf8("bStop"))
        self.horizontalLayout.addWidget(self.bStop)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lActual = QtGui.QLabel(self.centralwidget)
        self.lActual.setObjectName(_fromUtf8("lActual"))
        self.horizontalLayout.addWidget(self.lActual)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bClear = QtGui.QPushButton(self.centralwidget)
        self.bClear.setObjectName(_fromUtf8("bClear"))
        self.horizontalLayout.addWidget(self.bClear)
        self.bExport = QtGui.QPushButton(self.centralwidget)
        self.bExport.setObjectName(_fromUtf8("bExport"))
        self.horizontalLayout.addWidget(self.bExport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lCursor1 = QtGui.QLabel(self.centralwidget)
        self.lCursor1.setObjectName(_fromUtf8("lCursor1"))
        self.horizontalLayout_5.addWidget(self.lCursor1)
        self.lCursor2 = QtGui.QLabel(self.centralwidget)
        self.lCursor2.setObjectName(_fromUtf8("lCursor2"))
        self.horizontalLayout_5.addWidget(self.lCursor2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lDiff = QtGui.QLabel(self.centralwidget)
        self.lDiff.setText(_fromUtf8(""))
        self.lDiff.setObjectName(_fromUtf8("lDiff"))
        self.horizontalLayout_5.addWidget(self.lDiff)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cCursor1.setText(_translate("MainWindow", "Cursor 1", None))
        self.cCursor2.setText(_translate("MainWindow", "Cursor 2", None))
        self.bStart.setText(_translate("MainWindow", "Inicia", None))
        self.bPause.setText(_translate("MainWindow", "Pausa", None))
        self.bStop.setText(_translate("MainWindow", "Para", None))
        self.lActual.setText(_translate("MainWindow", "C", None))
        self.bClear.setText(_translate("MainWindow", "Limpia", None))
        self.bExport.setText(_translate("MainWindow", "Exporta", None))
        self.lCursor1.setText(_translate("MainWindow", "t: T:", None))
        self.lCursor2.setText(_translate("MainWindow", "t: T:", None))

from qwt_plot import QwtPlot
