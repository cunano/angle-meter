#!/usr/bin/env python
# -*- coding:utf-8 -*-

#system imports
import sys

#pyqt imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen

#numpy imports
from numpy import arctan, pi, sqrt

class MainWindow(QtWidgets.QWidget):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)

        self.m_DragPosition=self.pos()
        self.setStyleSheet("background-color:#1E361E;")

        self.setWindowOpacity(0.75)

        self.showFullScreen()

        self.setMouseTracking(False)

        self.pos_x0 = -20
        self.pos_y0 = -20

        self.pos_x = -20
        self.pos_y = -20


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        if self.pos_x0 == -20:
            pass
        else:
            pen = QPen(Qt.white, 2, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.pos_x0, self.pos_y0, self.pos_x, self.pos_y)
            dy = self.pos_y - self.pos_y0
            dx = self.pos_x - self.pos_x0
            if dx == 0:
                theta = 0.5*pi
            else:
                theta = arctan(dy/dx)
            theta *= 180/pi
            length = int(sqrt(dx**2 +  dy**2)*10)/10
            font = painter.font()
            font.setPointSize(18)
            painter.setFont(font)
            painter.drawText(self.pos_x, self.pos_y, str(int(abs(theta)*100)/100) + " deg, " + str(length) + " px")
        painter.end()


    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        if event.buttons() == Qt.LeftButton:
            self.pos_x0 = x
            self.pos_y0 = y

    
    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        if event.buttons() == Qt.RightButton:
            self.pos_x0 = x
            self.pos_y0 = y
        if event.buttons() == Qt.MiddleButton:
            self.pos_x = x
            self.pos_y = y
        if event.buttons() == Qt.LeftButton:
            self.pos_x = x
            self.pos_y = y
        self.update()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.showFullScreen()
        if event.key() == QtCore.Qt.Key_Escape:
            self.showNormal()

if __name__=="__main__":

    mapp=QtWidgets.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(mapp.exec_())
