# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\usuario\OneDrive\Documentos\semestre 2021-3\sistemas operativos\FInal\ventanaP.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qt_for_python.rcc.source import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1548, 682)
        MainWindow.setStyleSheet("*{\n"
" \n"
"    font-family: Comic Sans Ms;\n"
"    background-image:url(:/imagenes/imagenes/HD-wallpaper-abstract-colorful-colors-pattern-thumbnail.jpg);\n"
"}\n"
"\n"
"QPushButton{\n"
"   background:#2d89ef;\n"
"   color: white;\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   font-size:15px;        \n"
"}\n"
"\n"
"QFrame{\n"
"    /*background: rgb(0, 0, 0) transparent;\n"
"    border:transparent;*/\n"
"}\n"
"\n"
"QTableView {\n"
"    color: white;\n"
"    font-size:14px;\n"
"    background: rgb(59, 89, 213);\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   \n"
"}\n"
"\n"
"\n"
"QHeaderView{\n"
"  qproperty-defaultAlignment: AlignHCenter;\n"
"  background: rgb(59, 89, 213);\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QComboBox{\n"
"   background:#2d89ef;\n"
"   color: white;\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   font-size:15px;        \n"
"}\n"
"\n"
"QLabel{\n"
"    background: rgb(0, 0, 0) transparent;    \n"
"    color:white;\n"
"    font-weight: 900;\n"
"     font-size:18px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_bloquear = QtWidgets.QPushButton(self.centralwidget)
        self.boton_bloquear.setGeometry(QtCore.QRect(790, 630, 111, 41))
        self.boton_bloquear.setObjectName("boton_bloquear")
        self.boton_simular = QtWidgets.QPushButton(self.centralwidget)
        self.boton_simular.setGeometry(QtCore.QRect(610, 630, 111, 41))
        self.boton_simular.setObjectName("boton_simular")
        self.boton_agregarSrt = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregarSrt.setGeometry(QtCore.QRect(170, 30, 191, 31))
        self.boton_agregarSrt.setObjectName("boton_agregarSrt")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(520, 70, 501, 221))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 70, 491, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 1, 491, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 300, 1471, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(1030, 70, 501, 221))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.boton_agregarRound = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregarRound.setGeometry(QtCore.QRect(670, 30, 221, 31))
        self.boton_agregarRound.setObjectName("boton_agregarRound")
        self.boton_agregarFIFO = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregarFIFO.setGeometry(QtCore.QRect(1180, 30, 221, 31))
        self.boton_agregarFIFO.setObjectName("boton_agregarFIFO")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_bloquear.setText(_translate("MainWindow", "Bloquear"))
        self.boton_simular.setText(_translate("MainWindow", "Simular"))
        self.boton_agregarSrt.setText(_translate("MainWindow", "Agregar Cola srt"))
        self.boton_agregarRound.setText(_translate("MainWindow", "Agregar Cola Round Robin"))
        self.boton_agregarFIFO.setText(_translate("MainWindow", "Agregar Cola FIFO"))