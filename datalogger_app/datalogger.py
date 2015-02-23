#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import signal
import csv
from math import sin

import serial

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, Qt
import PyQt4.Qwt5 as Qwt


import main_ui

dt = 0.05

class BaseCommThread(QtCore.QThread):
    new_data = pyqtSignal(float, list)
    connected = pyqtSignal(unicode)
    disconnected = pyqtSignal()

    def __init__(self, parent=None):
        super(BaseCommThread, self).__init__(parent)
        self.t = 0
        self.dt = 0.05

    def run(self):
        while True:
            self.msleep(1000)

class MockCommThread(BaseCommThread):
    def calc(self):
        t = self.t
        y = sin(3.14159*t) * sin(3.14159*t*0.1)
        d0 = 0
        if y > 0:
            d0 = 1
        self.t += self.dt
        self.new_data.emit(t,[y,d0])

    def run(self):
        while True:
            self.calc()
            self.msleep( int(self.dt * 1000) )

class CommThread(BaseCommThread):
    def __init__(self, parent=None, port=None):
        super(CommThread, self).__init__(parent)
        self.port = port or '/dev/ttyUSB0'
        self._serial = serial.Serial(baudrate=115200, timeout=1)
        self.sampleIdx = 0
        self.connect(port)

    def disconnect(self):
        if self._serial.isOpen():
            self.disconnected.emit()
        self._serial.close()

    def connect(self, port=None):
        self.disconnect()
        port = port or self.port
        self._serial.setPort(port)
        try:
            self._serial.open()
            self._serial.flushInput()
            self.connected.emit(port)
            return True

        except serial.SerialException:
            return False
        return False

    def run(self):
        while True:
            try:
                line  = self._serial.readline()
                data = [float(x) for x in line.split()]
                t = self.t
                self.t += self.dt
                self.new_data.emit(t, data)
            except:
                if self.connect():
                    continue
                self.sleep(1)

class Datalogger(object):
    def __init__(self):
        win = main_ui.QtGui.QMainWindow()
        self.win = win
        self.xs = []
        self.ys = []
        self.ds = []
        self.sampleIdx = 0
        self.paused = False
        self.stopped = False
        self.windowLength = 60
        self.position = 0

        self.worker = MockCommThread()
        self.worker = CommThread()
        self.worker.new_data.connect(self.onNewData)

        uiplot = main_ui.Ui_MainWindow()
        uiplot.setupUi(win)
        self.uiplot = uiplot

        uiplot.bClear.clicked.connect(self.reset)
        uiplot.bStart.clicked.connect(self.onStart)
        uiplot.bStop.clicked.connect(self.onStop)
        uiplot.bPause.clicked.connect(self.onPause)
        uiplot.bExport.clicked.connect(self.onExport)
        uiplot.xScroll.sliderMoved.connect(self.onSlide)
        uiplot.scWinLength.valueChanged.connect(self.onWinLengthChange)

        uiplot.qwtPlot.setAxisScale( Qwt.QwtPlot.yRight, 0, 2)

        c=Qwt.QwtPlotCurve()
        c.setYAxis( Qwt.QwtPlot.yLeft)
        c.setPen(QtGui.QPen(Qt.blue))
        #c.setRenderHint(Qwt.QwtPlotItem.RenderAntialiased);
        c.attach(uiplot.qwtPlot)
        self.c = c

        dc=Qwt.QwtPlotCurve()
        dc.setYAxis( Qwt.QwtPlot.yRight)
        dc.setPen(QtGui.QPen(Qt.red))
        #dc.setRenderHint(Qwt.QwtPlotItem.RenderAntialiased);
        dc.attach(uiplot.qwtPlot)
        self.dc = dc

        self.cursor1 = self._buildCursor()
        self.cursor1.setLinePen(QtGui.QPen(Qt.red, 2, Qt.DashDotLine))
        self.cursor1.attach(self.uiplot.qwtPlot)

        self.cursor2 = self._buildCursor()
        self.cursor2.setLinePen(QtGui.QPen(Qt.green, 2, Qt.DashDotLine))
        self.cursor2.attach(self.uiplot.qwtPlot)

        self.cursors = []
        self.cursors.append([self.cursor1, uiplot.cCursor1, uiplot.sCursor1, uiplot.lCursor1])
        self.cursors.append([self.cursor2, uiplot.cCursor1, uiplot.sCursor2, uiplot.lCursor2])

        uiplot.cCursor1.toggled.connect(lambda visible: self.toggleCursor(0, visible))
        uiplot.cCursor2.toggled.connect(lambda visible: self.toggleCursor(1, visible))
        uiplot.sCursor1.valueChanged.connect(self.updateCursors)
        uiplot.sCursor2.valueChanged.connect(self.updateCursors)

        self.reset()
        win.show()

    def _buildCursor(self):
        m = Qwt.QwtPlotMarker()
        m.setValue(5.0, 1.0)
        m.setLineStyle(Qwt.QwtPlotMarker.Cross)
        m.setVisible(False)
        return m

    def toggleCursor(self, idx, visible):
        cursor = self.cursors[idx][0]
        cursor.setVisible(visible)
        self.uiplot.qwtPlot.replot()

    def moveCursor(self, cidx, xpos):
        cursor = self.cursors[cidx][0]
        label = self.cursors[cidx][3]
        offset = self.windowLength - xpos * self.windowLength / 1000.0
        xpos = self.position - offset
        ypos = 0

        if self.xs:
            idx = int(xpos / dt)
            if idx < len(self.ys):
                xpos = self.xs[idx]
                ypos = self.ys[idx]

        cursor.setValue(xpos, ypos)
        label.setText("Cursor: %i t: %.2f seg T: %.2f C" % (cidx, xpos, ypos))
        #print 'move cursor: xpos: %.2f ypos: %.2f' % (xpos, ypos)



    def updateCursors(self):
        doPlot = False
        for idx,(cursor, check, scroll, label) in enumerate(self.cursors):
            self.moveCursor(idx, scroll.value())
            if cursor.isVisible():
                doPlot = True
        if doPlot:
            self.uiplot.qwtPlot.replot()
        dt = self.cursor2.xValue() - self.cursor1.xValue()
        dT = self.cursor2.yValue() - self.cursor1.yValue()
        self.uiplot.lDiff.setText("dt: %.2f segundos dT: %.2f C" %(dt, dT))

    def onPause(self, paused):
        self.paused = paused

    def onStart(self):
        if not self.worker.isRunning():
            self.worker.start()

        self.stopped = False

    def onStop(self):
        self.stopped = True

    def onExport(self):
        fname = QtGui.QFileDialog.getSaveFileName(self.win, "Exportar...", "", "*.csv")
        if not fname:
            return

        stopped = self.stopped
        self.stopped = True

        f = open(fname, 'wb')
        writer = csv.writer(f)
        for idx in xrange(len(self.xs)):
            row = (self.xs[idx], self.ys[idx], self.ds[idx])
            writer.writerow(row)
        f.close()

        self.stopped = stopped

    def onSlide(self, pos):
        self.setPosition(pos)

    def setPosition(self, pos):
        length = self.windowLength

        start = pos-length
        end = pos
        if start < 0:
            start = 0
        if end < length:
            end = length

        self.position = end
        self.uiplot.qwtPlot.setAxisScale( Qwt.QwtPlot.xBottom, start, end)
        self.updateCursors()
        self.uiplot.qwtPlot.replot()

    def onWinLengthChange(self, length):
        pos = self.position
        t = length
        if self.xs:
            t = self.xs[-1]

        if self.position >= self.windowLength:
            pos = self.position - (self.windowLength / 2)
        if pos > t:
            pos = t

        if length < self.windowLength:
            self.uiplot.xScroll.setMaximum(t)

        self.uiplot.xScroll.setMinimum(length)

        self.windowLength = length
        self.setPosition(pos)
        self.uiplot.xScroll.setValue(self.position)

        self.uiplot.lblZoom.setText("Mostrar ventana de %i segundos" % length)

    def reset(self):
        stopped = self.stopped
        self.stopped = True

        self.xs = []
        self.ys = []
        self.ds = []
        self.setPosition(0)
        self.uiplot.xScroll.setMaximum(self.windowLength)
        self.uiplot.xScroll.setMinimum(self.windowLength)
        self.onWinLengthChange(self.windowLength)
        self.c.setData(self.xs, self.ys)
        self.uiplot.qwtPlot.replot()

        self.stopped = stopped


    def onNewData(self, t, data):
        if self.stopped:
            return

        if t > self.windowLength:
            self.uiplot.xScroll.setMaximum(t)

        try:
            y, d0 = data
        except:
            print 'BAD DATA: ', data
            return

        self.xs.append(t)
        self.ys.append(y)
        self.ds.append(d0)


        self.sampleIdx += 1
        if self.sampleIdx % 20 == 0:
            self.uiplot.lActual.setText('%.2f C' % y)

        if self.sampleIdx % 4 == 0:
            if not self.paused:
                self.c.setData(self.xs, self.ys)
                self.dc.setData(self.xs, self.ds)
                self.uiplot.xScroll.setValue(t)
                self.setPosition(t)



if __name__ == "__main__":
    qtapp = QtGui.QApplication(sys.argv)

    def sigint_handler(*args):
        qtapp.quit()
    signal.signal(signal.SIGINT, sigint_handler)

    app = Datalogger()

    sys.exit(qtapp.exec_())

