from wsprops import HSDiag
from wsprops import Visc
from math import pi
from math import sqrt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import logging


# Создание и подключение интерфейса
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1050, 820)
        mainWindow.setMinimumSize(QtCore.QSize(1050, 820))
        mainWindow.setMaximumSize(QtCore.QSize(1050, 820))
        mainWindow.setBaseSize(QtCore.QSize(1050, 820))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../HydroProga/Materials/water.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        mainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1040, 810))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("border-color: rgb(100, 100, 100);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 531, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(280, 40, 73, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                    "alternate-background-color: rgb(232, 232, 232);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 80, 73, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                      "alternate-background-color: rgb(232, 232, 232);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(280, 120, 110, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                      "alternate-background-color: rgb(232, 232, 232);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setGeometry(QtCore.QRect(280, 250, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_19.setGeometry(QtCore.QRect(280, 210, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_20.setGeometry(QtCore.QRect(280, 170, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 60, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_14.setGeometry(QtCore.QRect(410, 170, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_15.setGeometry(QtCore.QRect(410, 210, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_16.setGeometry(QtCore.QRect(410, 250, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 330, 621, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_17.setGeometry(QtCore.QRect(490, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_18.setGeometry(QtCore.QRect(490, 80, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setGeometry(QtCore.QRect(490, 120, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(360, 120, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(360, 80, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(360, 40, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 510, 621, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 80, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 120, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(370, 120, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_20.setGeometry(QtCore.QRect(500, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_21.setGeometry(QtCore.QRect(500, 80, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_22.setGeometry(QtCore.QRect(500, 120, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(370, 80, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(370, 40, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                       "alternate-background-color: rgb(232, 232, 232);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 710, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("alternate-background-color: rgb(232, 232, 232);")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(380, 690, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(640, 0, 391, 651))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../../../../HydroProga/Materials/ПВД.png"))
        self.label_13.setObjectName("label_13")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab)
        self.pushButton_23.setGeometry(QtCore.QRect(730, 700, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 561, 311))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(220, 70, 21, 21))
        self.label_9.setMinimumSize(QtCore.QSize(21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                   "gridline-color: rgb(0, 0, 0);\n"
                                   "border-color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(240, 70, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(250, 70, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(290, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(380, 70, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(10, 100, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(280, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(320, 100, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(330, 100, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(370, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setGeometry(QtCore.QRect(10, 130, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_4)
        self.label_30.setGeometry(QtCore.QRect(270, 130, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(310, 130, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(320, 130, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(360, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(10, 160, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(130, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_4)
        self.label_37.setGeometry(QtCore.QRect(170, 160, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_4)
        self.label_38.setGeometry(QtCore.QRect(180, 160, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_4)
        self.label_39.setGeometry(QtCore.QRect(230, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.groupBox_4)
        self.label_41.setGeometry(QtCore.QRect(10, 190, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_4)
        self.label_42.setGeometry(QtCore.QRect(210, 190, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_4)
        self.label_43.setGeometry(QtCore.QRect(240, 190, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_4)
        self.label_44.setGeometry(QtCore.QRect(250, 190, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.groupBox_4)
        self.label_45.setGeometry(QtCore.QRect(280, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_47 = QtWidgets.QLabel(self.groupBox_4)
        self.label_47.setGeometry(QtCore.QRect(10, 220, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.groupBox_4)
        self.label_48.setGeometry(QtCore.QRect(330, 220, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.groupBox_4)
        self.label_49.setGeometry(QtCore.QRect(360, 220, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_4)
        self.label_50.setGeometry(QtCore.QRect(370, 220, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_4)
        self.label_51.setGeometry(QtCore.QRect(410, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_53 = QtWidgets.QLabel(self.groupBox_4)
        self.label_53.setGeometry(QtCore.QRect(10, 250, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_4)
        self.label_54.setGeometry(QtCore.QRect(330, 250, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_4)
        self.label_55.setGeometry(QtCore.QRect(370, 250, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_4)
        self.label_56.setGeometry(QtCore.QRect(380, 250, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.groupBox_4)
        self.label_57.setGeometry(QtCore.QRect(410, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.label_59 = QtWidgets.QLabel(self.groupBox_4)
        self.label_59.setGeometry(QtCore.QRect(10, 280, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.groupBox_4)
        self.label_60.setGeometry(QtCore.QRect(320, 280, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_60.setText("")
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.groupBox_4)
        self.label_61.setGeometry(QtCore.QRect(360, 280, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.groupBox_4)
        self.label_62.setGeometry(QtCore.QRect(370, 280, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_62.setText("")
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.groupBox_4)
        self.label_63.setGeometry(QtCore.QRect(410, 280, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(460, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(450, 130, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_34.setObjectName("label_34")
        self.label_40 = QtWidgets.QLabel(self.groupBox_4)
        self.label_40.setGeometry(QtCore.QRect(320, 160, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_40.setObjectName("label_40")
        self.label_46 = QtWidgets.QLabel(self.groupBox_4)
        self.label_46.setGeometry(QtCore.QRect(370, 190, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_46.setObjectName("label_46")
        self.label_52 = QtWidgets.QLabel(self.groupBox_4)
        self.label_52.setGeometry(QtCore.QRect(500, 220, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_52.setObjectName("label_52")
        self.label_58 = QtWidgets.QLabel(self.groupBox_4)
        self.label_58.setGeometry(QtCore.QRect(500, 250, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_58.setObjectName("label_58")
        self.label_64 = QtWidgets.QLabel(self.groupBox_4)
        self.label_64.setGeometry(QtCore.QRect(500, 280, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_64.setObjectName("label_64")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 340, 621, 281))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_65 = QtWidgets.QLabel(self.groupBox_5)
        self.label_65.setGeometry(QtCore.QRect(10, 40, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.groupBox_5)
        self.label_66.setGeometry(QtCore.QRect(550, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_66.setObjectName("label_66")
        self.label_68 = QtWidgets.QLabel(self.groupBox_5)
        self.label_68.setGeometry(QtCore.QRect(10, 70, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.label_79 = QtWidgets.QLabel(self.groupBox_5)
        self.label_79.setGeometry(QtCore.QRect(10, 100, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.label_82 = QtWidgets.QLabel(self.groupBox_5)
        self.label_82.setGeometry(QtCore.QRect(10, 130, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.label_85 = QtWidgets.QLabel(self.groupBox_5)
        self.label_85.setGeometry(QtCore.QRect(10, 160, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.groupBox_5)
        self.label_86.setGeometry(QtCore.QRect(10, 190, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.groupBox_5)
        self.label_87.setGeometry(QtCore.QRect(10, 220, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.groupBox_5)
        self.label_88.setGeometry(QtCore.QRect(10, 250, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.label_75 = QtWidgets.QLabel(self.groupBox_5)
        self.label_75.setGeometry(QtCore.QRect(500, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.groupBox_5)
        self.label_76.setGeometry(QtCore.QRect(520, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.groupBox_5)
        self.label_77.setGeometry(QtCore.QRect(380, 160, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_77.setObjectName("label_77")
        self.label_69 = QtWidgets.QLabel(self.groupBox_5)
        self.label_69.setGeometry(QtCore.QRect(550, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_5)
        self.label_70.setGeometry(QtCore.QRect(460, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.groupBox_5)
        self.label_71.setGeometry(QtCore.QRect(480, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.groupBox_5)
        self.label_72.setGeometry(QtCore.QRect(350, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_72.setObjectName("label_72")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 640, 1001, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_67 = QtWidgets.QLabel(self.groupBox_6)
        self.label_67.setGeometry(QtCore.QRect(10, 30, 701, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_67.setText("")
        self.label_67.setObjectName("label_67")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_24.setGeometry(QtCore.QRect(760, 80, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_25.setGeometry(QtCore.QRect(730, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_73 = QtWidgets.QLabel(self.tab_3)
        self.label_73.setGeometry(QtCore.QRect(660, 10, 345, 412))
        self.label_73.setText("")
        self.label_73.setPixmap(QtGui.QPixmap("../../../../HydroProga/Materials/Схема2.png"))
        self.label_73.setObjectName("label_73")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(690, 420, 267, 226))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("../../../../HydroProga/Materials/Спираль2.png"))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_3, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Гидравлический расчет ПВД"))
        self.groupBox.setTitle(_translate("mainWindow", "Компоновочные характеристики"))
        self.label.setText(_translate("mainWindow", "Тип спирального элемента"))
        self.label_2.setText(_translate("mainWindow", "Число колонн"))
        self.label_3.setText(_translate("mainWindow", "Типоразмер по габариту"))
        self.comboBox.setItemText(0, _translate("mainWindow", "1"))
        self.comboBox.setItemText(1, _translate("mainWindow", "2"))
        self.comboBox.setItemText(2, _translate("mainWindow", "3"))
        self.comboBox.setItemText(3, _translate("mainWindow", "4"))
        self.comboBox.setItemText(4, _translate("mainWindow", "5"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "4"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "6"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "Малый"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "Средний"))
        self.comboBox_3.setItemText(2, _translate("mainWindow", "Крупный"))
        self.label_4.setText(_translate("mainWindow", "Число рядов СЭ в зоне ОК"))
        self.label_5.setText(_translate("mainWindow", "Число рядов СЭ в зоне КП"))
        self.label_6.setText(_translate("mainWindow", "Число рядов СЭ в зоне ОП"))
        self.pushButton_12.setText(_translate("mainWindow", "Ок"))
        self.pushButton_14.setText(_translate("mainWindow", "Ок"))
        self.pushButton_15.setText(_translate("mainWindow", "Ок"))
        self.pushButton_16.setText(_translate("mainWindow", "Ок"))
        self.groupBox_2.setTitle(_translate("mainWindow", "Режимные характеристики"))
        self.label_10.setText(_translate("mainWindow", "Расход питательной воды, кг/с"))
        self.label_11.setText(_translate("mainWindow", "Доля воды, направляемая в зону ОК, %"))
        self.label_12.setText(_translate("mainWindow", "Доля воды, направляемая в зону ОП, %"))
        self.pushButton_17.setText(_translate("mainWindow", "Ок"))
        self.pushButton_18.setText(_translate("mainWindow", "Ок"))
        self.pushButton_19.setText(_translate("mainWindow", "Ок"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Параметры теплоносителя"))
        self.label_16.setWhatsThis(_translate("mainWindow",
                                              "<html><head/><body><p><span style=\" vertical-align:super;\">0</span></p></body></html>"))
        self.label_16.setText(_translate("mainWindow",
                                         "<html><head/><body><p>Температура воды на входе в ПВД, <span style=\" vertical-align:super;\">0</span>С</p></body></html>"))
        self.label_17.setText(_translate("mainWindow",
                                         "<html><head/><body><p>Температура воды на выходе из ПВД, <span style=\" vertical-align:super;\">0</span>С</p></body></html>"))
        self.label_18.setText(_translate("mainWindow", "Давление воды на входе в ПВД, кПа"))
        self.pushButton_20.setText(_translate("mainWindow", "Ок"))
        self.pushButton_21.setText(_translate("mainWindow", "Ок"))
        self.pushButton_22.setText(_translate("mainWindow", "Ок"))
        self.checkBox.setText(_translate("mainWindow", "Упрощенная методика расчета"))
        self.pushButton_10.setText(_translate("mainWindow", "Рассчитать"))
        self.pushButton_23.setText(_translate("mainWindow", "Справка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Исходные данные"))
        self.groupBox_4.setTitle(_translate("mainWindow", "Конструктивные характеристики"))
        self.label_7.setText(_translate("mainWindow", "Тип: Труба стальная бесшовная ГОСТ 8732-78"))
        self.label_8.setText(_translate("mainWindow", "1. Спиральный элемент"))
        self.label_9.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_19.setText(_translate("mainWindow", "х"))
        self.label_20.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_21.setText(_translate("mainWindow", "Длина, м"))
        self.label_22.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_23.setText(_translate("mainWindow", "2. Входной/выходной патрубок"))
        self.label_24.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_25.setText(_translate("mainWindow", "х"))
        self.label_26.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_27.setText(_translate("mainWindow", "Длина, м"))
        self.label_29.setText(_translate("mainWindow", "3. Подводящий трубопровод"))
        self.label_30.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_31.setText(_translate("mainWindow", "х"))
        self.label_32.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_33.setText(_translate("mainWindow", "Длина, м"))
        self.label_35.setText(_translate("mainWindow", "4. Коллектор"))
        self.label_36.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_37.setText(_translate("mainWindow", "х"))
        self.label_38.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_39.setText(_translate("mainWindow", "Длина, м"))
        self.label_41.setText(_translate("mainWindow", "5. Коллектор зоны ОК"))
        self.label_43.setText(_translate("mainWindow", "х"))
        self.label_45.setText(_translate("mainWindow", "Длина, м"))
        self.label_47.setText(_translate("mainWindow", "6. Отводящий трубопровод зоны ОК"))
        self.label_49.setText(_translate("mainWindow", "х"))
        self.label_51.setText(_translate("mainWindow", "Длина, м"))
        self.label_53.setText(_translate("mainWindow", "7. Отводящий трубопровод зоны ОП"))
        self.label_55.setText(_translate("mainWindow", "х"))
        self.label_57.setText(_translate("mainWindow", "Длина, м"))
        self.label_59.setText(_translate("mainWindow", "8. Отводящяя магистраль зоны ОП"))
        self.label_61.setText(_translate("mainWindow", "х"))
        self.label_63.setText(_translate("mainWindow", "Длина, м"))
        self.label_28.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_34.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_40.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_46.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_52.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_58.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_64.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.groupBox_5.setTitle(_translate("mainWindow", "Гидравлические характеристики"))
        self.label_65.setText(_translate("mainWindow", "Абсолютные потери давления питательной воды в ПВД, кПа"))
        self.label_66.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_68.setText(_translate("mainWindow", "Относительные потери давления питательной воды в ПВД, %"))
        self.label_79.setText(_translate("mainWindow", "Полные потери давления в спиральных элементах, кПа"))
        self.label_82.setText(_translate("mainWindow", "Полные потери давления в местных сопротивлениях, кПа"))
        self.label_85.setText(_translate("mainWindow", "Полные потери давления на трение, кПа"))
        self.label_86.setText(_translate("mainWindow", "Доля потерь давления в спиральных элементах, %"))
        self.label_87.setText(_translate("mainWindow", "Доля потерь давления в местных сопротивлениях, %"))
        self.label_88.setText(_translate("mainWindow", "Доля потерь давления в на трение, %"))
        self.label_75.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_76.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_77.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_69.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_70.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_71.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_72.setText(
            _translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.groupBox_6.setTitle(_translate("mainWindow", "Рекомендации"))
        self.pushButton_24.setText(_translate("mainWindow", "Новый расчет"))
        self.pushButton_25.setText(_translate("mainWindow", "Сохранить результаты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "Результаты расчета"))


# Обработка ошибок и запись логов в файл
class MyError(Exception):
    def __init__(self, error_text):
        self.txt = error_text
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.setText(error_text)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../HydroProga/Materials/water.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        error.setWindowIcon(icon)
        error.exec_()
        logging.basicConfig(level=logging.DEBUG, filename="C:\\HydroProga\HydroLog.txt",
                            format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                            datefmt='%H:%M:%S')


# Создание справки
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 333)
        Form.setMinimumSize(QtCore.QSize(932, 333))
        Form.setMaximumSize(QtCore.QSize(932, 333))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../HydroProga/Materials/water.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 920, 330))
        self.label.setMinimumSize(QtCore.QSize(920, 330))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Справка"))
        self.label.setText(_translate("Form", "Все подогреватели в зависимости от числа спиральных элементов (СЭ) (в "
                                              "пересчёте на число \n "
                                              "плоскостей) можно разделить по габаритам на малые (М) c числом СЭ Nсп = 100..400,\n"
                                              "средние (С) − Nсп = 400..800 и большие (Б) − Nсп = 800..1200. \n"
                                              "В данном случае величина Nсп определяется следующим образом:\n"
                                              "Nсп = Nкол * (Nок * Nкп * Nоп).\n"
                                              "\n"
                                              "Типы применяемых СЭ:\n"
                                              "1. dвш×δтр, мм - 22×3.5. nпл = 1, Dгиб, мм = 98, nв = 7, Lсп, м = 6.94, Dнр, м = 0.5\n"
                                              "2. dвш×δтр, мм - 32×4. nпл = 1, Dгиб, мм = 200, nв = 9, Lсп, м = 17.92, Dнр, м = 0.97\n"
                                              "3. dвш×δтр, мм - 32×4. nпл = 2, Dгиб, мм = 200, nв = 9, Lсп, м = 35.84, Dнр, м = 0.97\n"
                                              "4. dвш×δтр, мм - 32×5. nпл = 1, Dгиб, мм = 240, nв = 9, Lсп, м = 20.06, Dнр, м = 1.05\n"
                                              "5. dвш×δтр, мм - 32×5. nпл = 2, Dгиб, мм = 240, nв = 9, Lсп, м = 40.11, Dнр, м = 1.05"))


# Подключение справки
class Help_Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# Подключение интерфейса
class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_state()
        self.button_func()

    # Запрет на редактирование и установка цвета
    def load_state(self):
        self.lineEdit_12.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_13.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_14.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_15.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_16.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_17.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_18.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_19.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_20.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_20.setReadOnly(True)
        self.checkBox.setDisabled(True)
        self.pushButton_10.setDisabled(True)
        self.pushButton_25.setDisabled(True)
        global base_flag
        global N_ok_flag
        global N_kp_flag
        global N_op_flag
        global Wpv_flag
        global X_Ok_flag
        global X_Op_flag
        global t_In_flag
        global t_Out_flag
        global p_In_flag
        base_flag = False
        N_ok_flag = False
        N_kp_flag = False
        N_op_flag = False
        Wpv_flag = False
        X_Ok_flag = False
        X_Op_flag = False
        t_In_flag = False
        t_Out_flag = False
        p_In_flag = False

        # Функционал кнопок
    def button_func(self):
        self.pushButton_12.clicked.connect(self.write_base_data)
        self.pushButton_14.clicked.connect(self.write_data_N_ok)
        self.pushButton_15.clicked.connect(self.write_data_N_kp)
        self.pushButton_16.clicked.connect(self.write_data_N_op)
        self.pushButton_17.clicked.connect(self.write_data_Wpv)
        self.pushButton_18.clicked.connect(self.write_data_X_ok)
        self.pushButton_19.clicked.connect(self.write_data_X_op)
        self.pushButton_20.clicked.connect(self.write_data_t_in)
        self.pushButton_21.clicked.connect(self.write_data_t_out)
        self.pushButton_22.clicked.connect(self.write_data_p_in)
        self.pushButton_23.clicked.connect(self.help_ex)
        self.pushButton_24.clicked.connect(self.restart)
        self.pushButton_25.clicked.connect(self.save_res)
        self.checkBox.clicked.connect(self.choose_metod)
        self.pushButton_10.clicked.connect(self.w_d_retrieve)
        self.pushButton_10.clicked.connect(self.calc_process)
        self.pushButton_10.clicked.connect(self.show_results)

    # Функция вызова справки
    def help_ex(self):
        self.Help = Help_Window()
        self.Help.show()

    # Запись результатов в файл
    def save_res(self):
        my_file = open("C:\\HydroProga\Results.txt", 'a')
        my_file.write(str(Type_Config) + '\n')
        my_file.write(str(ID) + '\n')
        if Metod == 'Полный':
            my_file.write('Абсолютные потери давления питательной воды в ПВД: {0} кПа.'.format(Delta_p_abs) + '\n')
            my_file.write(
                'Относительные потери давления питательной воды в ПВД: {0} %.'.format(Delta_p_comp) + '\n')
            my_file.write('Полные потери давления в спиральных элементах: {0} кПа.'.format(Delta_p_se) + '\n')
            my_file.write('Полные потери давления в местных сопротивлениях: {0} кПа.'.format(Delta_p_r) + '\n')
            my_file.write('Полные потери давления на трение: {0} кПа.'.format(Delta_p_f) + '\n')
            my_file.write('Доля потерь давления в спиральных элементах: {0} %.'.format(Delta_p_comp_se) + '\n')
            my_file.write('Доля потерь давления в местных сопротивлениях: {0} %.'.format(Delta_p_comp_r) + '\n')
            my_file.write('Доля потерь давления в на трение: {0} %.'.format(Delta_p_comp_f) + '\n')
            if Delta_p_abs < Config_Limits[5]:
                my_file.write(
                    'Потери давления ниже диапазона допустимых значений для данной компоновки. Необходимо '
                    'уменьшить число' + '\n')
                my_file.write(
                    'рядов спиралей в зонах, увеличить доли расхода воды, направляемой в зоны ОК и ОП или выбрать '
                    'другой' + '\n')
                my_file.write('тип компоновки.' + '\n')
                my_file.write('\n')
                my_file.close()
            elif Delta_p_abs > Config_Limits[6]:
                my_file.write(
                    'Потери давления выше диапазона допустимых значений для данной компоновки. Необходимо увеличить '
                    'число' + '\n')
                my_file.write(
                    'рядов спиралей в зонах, уменьшить доли расхода воды, направляемой в зоны ОК и ОП или выбрать '
                    'другой' + '\n')
                my_file.write('тип компоновки.' + '\n')
                my_file.write('\n')
                my_file.close()
            else:
                my_file.write('Гидравлический режим выбранной компоновки подогревателя удовлетворительный.' + '\n')
                my_file.write('\n')
                my_file.close()
        else:
            my_file.write('Абсолютные потери давления питательной воды в ПВД: {0} кПа.'.format(Delta_p_abs) + '\n')
            my_file.write(
                'Относительные потери давления питательной воды в ПВД: {0} %.'.format(Delta_p_comp) + '\n')
            my_file.write('Полные потери давления в спиральных элементах: {0} кПа.'.format(Delta_p_se) + '\n')
            if Delta_p_abs < Config_Limits[5]:
                my_file.write(
                    'Потери давления ниже диапазона допустимых значений для данной компоновки. Необходимо '
                    'уменьшить число' + '\n')
                my_file.write(
                    'рядов спиралей в зонах, увеличить доли расхода воды, направляемой в зоны ОК и ОП или выбрать '
                    'другой' + '\n')
                my_file.write('тип компоновки.' + '\n')
                my_file.write('\n')
                my_file.close()
            elif Delta_p_abs > Config_Limits[6]:
                my_file.write(
                    'Потери давления выше диапазона допустимых значений для данной компоновки. Необходимо увеличить '
                    'число' + '\n')
                my_file.write(
                    'рядов спиралей в зонах, уменьшить доли расхода воды, направляемой в зоны ОК и ОП или выбрать '
                    'другой' + '\n')
                my_file.write('тип компоновки.' + '\n')
                my_file.write('\n')
                my_file.close()
            else:
                my_file.write('Гидравлический режим выбранной компоновки подогревателя удовлетворительный.' + '\n')
                my_file.write('\n')
                my_file.close()

    def restart(self):
        self.label_9.clear()
        self.label_20.clear()
        self.label_24.clear()
        self.label_26.clear()
        self.label_30.clear()
        self.label_32.clear()
        self.label_36.clear()
        self.label_38.clear()
        self.label_42.clear()
        self.label_44.clear()
        self.label_48.clear()
        self.label_50.clear()
        self.label_54.clear()
        self.label_56.clear()
        self.label_60.clear()
        self.label_62.clear()
        self.label_22.clear()
        self.label_28.clear()
        self.label_34.clear()
        self.label_40.clear()
        self.label_46.clear()
        self.label_52.clear()
        self.label_58.clear()
        self.label_64.clear()
        self.label_66.clear()
        self.label_69.clear()
        self.label_75.clear()
        self.label_76.clear()
        self.label_77.clear()
        self.label_70.clear()
        self.label_71.clear()
        self.label_72.clear()
        self.label_67.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.lineEdit_16.clear()
        self.lineEdit_17.clear()
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_12.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_13.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_14.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_15.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_16.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_17.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_18.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_19.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_20.setStyleSheet("background-color: rgb(232, 232, 232)")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_20.setReadOnly(True)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.checkBox.setChecked(False)
        self.checkBox.setDisabled(True)
        self.pushButton_10.setDisabled(True)
        self.pushButton_25.setDisabled(True)

    # Характеристики спиральных элементов
    global char_SE
    char_SE = [(1, 22, 3.5, 3, 1, 7, 6.94, 0.5), (2, 32, 4, 4, 1, 9, 17.92, 0.97), (3, 32, 4, 4, 2, 9, 35.84, 0.97),
               (4, 32, 5, 4, 1, 9, 20.06, 1.05), (5, 32, 5, 4, 2, 9, 40.11, 1.05)]

    # Характеристики компоновок
    global char_Config
    char_Config = [(1, 4, 'Малый', 50, 75, 100, 200, 'Simple', 2, 4, 24, 48, 6, 12),
                   (1, 4, 'Средний', 100, 150, 100, 200, 'Full', 4, 8, 48, 96, 12, 24),
                   (1, 6, 'Малый', 50, 100, 40, 150, 'Simple', 2, 4, 24, 48, 6, 12),
                   (1, 6, 'Средний', 100, 200, 50, 200, 'Full', 4, 8, 48, 96, 12, 24),
                   (1, 6, 'Крупный', 300, 400, 200, 350, 'Full', 6, 12, 90, 144, 20, 36),
                   (2, 4, 'Малый', 50, 150, 40, 275, 'Full', 2, 4, 24, 48, 6, 12),
                   (2, 4, 'Средний', 100, 200, 50, 175, 'Full', 4, 8, 48, 96, 12, 24),
                   (3, 4, 'Малый', 50, 75, 200, 400, 'Simple', 2, 4, 24, 48, 6, 12),
                   (3, 4, 'Средний', 100, 150, 200, 400, 'Simple', 4, 8, 48, 96, 12, 24),
                   (2, 6, 'Малый', 50, 150, 20, 150, 'Full', 2, 4, 24, 48, 6, 12),
                   (2, 6, 'Средний', 100, 300, 20, 150, 'Full', 4, 8, 48, 96, 12, 24),
                   (4, 6, 'Крупный', 300, 600, 100, 300, 'Full', 6, 12, 90, 144, 20, 36),
                   (3, 6, 'Малый', 50, 100, 100, 350, 'Simple', 2, 4, 24, 48, 6, 12),
                   (3, 6, 'Средний', 100, 300, 100, 400, 'Simple', 4, 8, 48, 96, 12, 24),
                   (5, 6, 'Крупный', 300, 400, 400, 750, 'Simple', 6, 12, 90, 144, 20, 36)]

    # Применяемые трубы по ГОСТ
    global d2_GOST
    global d34_GOST
    global d56_GOST
    global d7_GOST
    global d8_GOST
    d2_GOST = [(201, 22, 221, 26, 225, 24), (291, 43, 273, 50, 361, 52), (361, 52, 400, 65)]
    d34_GOST = [(102, 22, 112, 20, 119, 20, 128, 20, 124, 22, 132, 24), (143, 30, 147, 36, 165, 40),
                (155, 45, 173, 50, 187, 56)]
    d56_GOST = [(52, 12), (67, 14, 80, 14), (67, 14, 80, 14, 82, 16)]
    d7_GOST = [(82, 16, 89, 16, 93, 20), (93, 20, 102, 22), (124, 22, 132, 24)]
    d8_GOST = [(128, 20, 132, 24), (128, 20, 132, 24, 143, 30, 147, 36), (165, 40, 155, 45, 173, 50)]

    # Рекомендуемые скорости
    global wRec
    wRec = [(3.0, 5.0, 2.0, 2.0, 2.0), (3.0, 5.0, 2.0, 2.0, 3.0), (4.5, 6.0, 2.5, 3.0, 4.5)]

    # Определение Дзета10 (выход из магистрали ОП в выходной патрубок)
    global dd82
    global WW28
    global dW
    dd82 = (0.1, 0.2, 0.3, 0.4)
    WW28 = (0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.43)
    dW = [(0.4, 2.1, 3.8, 6.5, 9.2, 12.75, 16.3, 19.06), (-0.37, 0.175, 0.72, 1.495, 2.27, 3.285, 4.3, 5.035),
          (-0.51, -0.17, 0.17, 0.585, 1, 1.53, 2.06, 2.41), (-0.54, -0.285, -0.03, 0.25, 0.58, 0.94, 1.3, 1.525)]

    # Сбор компоновки подогревателя от пользователя c учетом ограничений
    def write_base_data(self):
        global Metod
        global type_SE
        global Num_Col
        global type_Gab
        global base_flag
        Metod = 'Полный'
        base_flag = False
        self.comboBox.currentIndexChanged.connect(self.restart)
        self.comboBox_2.currentIndexChanged.connect(self.restart)
        self.comboBox_3.currentIndexChanged.connect(self.restart)
        type_SE = int(self.comboBox.currentText())
        Num_Col = int(self.comboBox_2.currentText())
        type_Gab = self.comboBox_3.currentText()
        try:
            if type_Gab == 'Крупный' and Num_Col == 4:
                raise MyError(
                    'Данный вариант компоновки не рекомендуется. Измените число колонн или габариты подогревателя.' + '\n')
            elif type_SE == 4 and (Num_Col == 4 or type_Gab != 'Крупный'):
                raise MyError('Данный тип спирального элемента применяется для крупных 6-ти колонных ПВД.' + '\n')
            elif type_SE == 5 and (Num_Col == 4 or type_Gab != 'Крупный'):
                raise MyError('Данный тип спирального элемента применяется для крупных 6-ти колонных ПВД.' + '\n')
            else:
                # Разрешение на редактирование и смена цвета
                base_flag = True
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
                self.lineEdit_12.setReadOnly(False)
                self.lineEdit_13.setReadOnly(False)
                self.lineEdit_14.setReadOnly(False)
                self.lineEdit_15.setReadOnly(False)
                self.lineEdit_16.setReadOnly(False)
                self.lineEdit_17.setReadOnly(False)
                self.lineEdit_18.setReadOnly(False)
                self.lineEdit_19.setReadOnly(False)
                self.lineEdit_20.setReadOnly(False)
                self.lineEdit_12.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_13.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_14.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_15.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_16.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_17.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_18.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_19.setStyleSheet("background-color: rgb(85, 255, 255)")
                self.lineEdit_20.setStyleSheet("background-color: rgb(85, 255, 255)")

                # Получение характеристик компоновки из массива и запись в файл
                global Type_Config
                Type_Config = (type_SE, Num_Col, type_Gab)
                for i in range(len(char_Config)):
                    a = char_Config[i]
                    if Type_Config == a[:3]:
                        global Config_Limits
                        Config_Limits = a
                        break

                # Получение характеристик спирального элемента из массива
                for i in range(len(char_SE)):
                    b = char_SE[i]
                    if type_SE == b[0]:
                        global Config_SE
                        Config_SE = b
                        break
                # Включение чекбокса с методикой
                if Config_Limits[7] == 'Simple':
                    self.checkBox.setDisabled(False)

        except MyError:
            base_flag = False
            if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                self.pushButton_10.setDisabled(False)
            else:
                self.pushButton_10.setDisabled(True)
            logging.exception('Выбрана недопустимая компоновка.')

    # Получение данных от пользователя c учетом ограничений
    def write_data_N_ok(self):
        global Config_SE
        global N_ok_flag
        global N_ok
        try:
            N_ok_flag = False
            N_ok_f = int(self.lineEdit_20.text())
            if N_ok_f <= 0:
                raise MyError('Значение отрицательно или равно 0' + '\n')
            elif N_ok_f < Config_Limits[8]:
                raise MyError('Число рядов спиральных элементов ниже допустимого предела.' + '\n')
            elif N_ok_f > Config_Limits[9]:
                raise MyError('Число рядов спиральных элементов выше допустимого предела.' + '\n')
            elif Config_SE[4] == 2 and N_ok_f % 2 != 0:
                raise MyError('Число рядов спиральных элементов при двухплоскостной спирали должно быть четным.' + '\n')
            else:
                N_ok_flag = True
                N_ok = N_ok_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_N_kp(self):
        global N_kp_flag
        global N_kp
        try:
            N_kp_flag = False
            N_kp_f = int(self.lineEdit_19.text())
            if N_kp_f <= 0:
                raise MyError('Значение отрицательно или равно 0' + '\n')
            elif N_kp_f < Config_Limits[10]:
                raise MyError('Число рядов спиральных элементов ниже допустимого предела.' + '\n')
            elif N_kp_f > Config_Limits[11]:
                raise MyError('Число рядов спиральных элементов выше допустимого предела.' + '\n')
            elif Config_SE[4] == 2 and N_kp_f % 2 != 0:
                raise MyError('Число рядов спиральных элементов при двухплоскостной спирали должно быть четным.' + '\n')
            else:
                N_kp_flag = True
                N_kp = N_kp_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_N_op(self):
        global N_op_flag
        global N_op
        try:
            N_op_flag = False
            N_op_f = int(self.lineEdit_18.text())
            if N_op_f <= 0:
                raise MyError('Значение отрицательно или равно 0' + '\n')
            elif N_op_f < Config_Limits[12]:
                raise MyError('Число рядов спиральных элементов ниже допустимого предела.' + '\n')
            elif N_op_f > Config_Limits[13]:
                raise MyError('Число рядов спиральных элементов выше допустимого предела.' + '\n')
            elif Config_SE[4] == 2 and N_op_f % 2 != 0:
                raise MyError('Число рядов спиральных элементов при двухплоскостной спирали должно быть четным.' + '\n')
            else:
                N_op_flag = True
                N_op = N_op_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_Wpv(self):
        global Wpv_flag
        global Wpv
        try:
            Wpv_flag = False
            Wpv_f = int(self.lineEdit_17.text())
            if Wpv_f <= 0:
                raise MyError('Значение отрицательно или равно 0' + '\n')
            elif Wpv_f < Config_Limits[3]:
                raise MyError('Расход питательной воды ниже допустимого предела.' + '\n')
            elif Wpv_f > Config_Limits[4]:
                raise MyError('Расход питательной воды выше допустимого предела.' + '\n')
            else:
                Wpv_flag = True
                Wpv = Wpv_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_X_ok(self):
        global X_Ok_flag
        global X_Ok
        try:
            X_Ok_flag = False
            X_Ok_f = int(self.lineEdit_16.text())
            if X_Ok_f <= 0:
                raise MyError('Значение отрицательно или равно 0' + '\n')
            elif X_Ok_f < 5:
                raise MyError('Значение ниже допустимого предела.' + '\n')
            elif X_Ok_f > 20:
                raise MyError('Значение выше допустимого предела.' + '\n')
            else:
                X_Ok_flag = True
                X_Ok = X_Ok_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_X_op(self):
        global X_Op_flag
        global X_Op
        try:
            X_Op_flag = False
            X_Op_f = int(self.lineEdit_15.text())
            if X_Op_f <= 0:
                raise MyError('Значение отрицательно или равно 0')
            elif X_Op_f < 10:
                raise MyError('Значение ниже допустимого предела.')
            elif X_Op_f > 30:
                raise MyError('Значение выше допустимого предела.')
            else:
                X_Op_flag = True
                X_Op = X_Op_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_t_in(self):
        global t_In_flag
        global t_In
        try:
            t_In_flag = False
            t_In_f = int(self.lineEdit_14.text())
            if t_In_f <= 0:
                raise MyError('Значение отрицательно или равно 0')
            elif t_In_f < 150:
                raise MyError('Значение ниже допустимого предела.')
            elif t_In_f > 265:
                raise MyError('Значение выше допустимого предела.')
            else:
                t_In_flag = True
                t_In = t_In_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_t_out(self):
        global t_Out_flag
        global t_Out
        try:
            t_Out_flag = False
            t_Out_f = int(self.lineEdit_13.text())
            if t_Out_f <= 0:
                raise MyError('Значение отрицательно или равно 0')
            elif t_Out_f < 150:
                raise MyError('Значение ниже допустимого предела.')
            elif t_Out_f > 265:
                raise MyError('Значение выше допустимого предела.')
            else:
                t_Out_flag = True
                t_Out = t_Out_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    def write_data_p_in(self):
        global p_In_flag
        global p_In
        try:
            p_In_flag = False
            p_In_f = int(self.lineEdit_12.text())
            if p_In_f <= 0:
                raise MyError('Значение отрицательно или равно 0')
            elif p_In_f < 15000:
                raise MyError('Давление ниже допустимого предела.')
            elif p_In_f > 30000:
                raise MyError('Давление выше допустимого предела.')
            else:
                p_In_flag = True
                p_In = p_In_f
                if base_flag * N_ok_flag * N_kp_flag * N_op_flag * Wpv_flag * X_Ok_flag * X_Op_flag * t_In_flag * t_Out_flag * p_In_flag == True:
                    self.pushButton_10.setDisabled(False)
                else:
                    self.pushButton_10.setDisabled(True)
        except MyError:
            logging.exception('Указано неверное значение!')
        except ValueError:
            logging.exception('Ошибка ввода данных!')
            MyError.error = QMessageBox()
            MyError.error.setWindowTitle("Ошибка!")
            MyError.error.setIcon(QMessageBox.Warning)
            MyError.error.setStandardButtons(QMessageBox.Ok)
            MyError.error.setText('Ошибка ввода данных! Необходимо ввести положительное число.')
            MyError.error.exec_()
            return

    # Упрощенная методика
    def choose_metod(self):
        global Metod
        if self.checkBox.isChecked():
            Metod = "Упрощенный"
        else:
            Metod = "Полный"

    # Получение значений из массивов рекомендуемых скоростей и диаметров
    def w_d_retrieve(self):
        checkTypeGab = ('Малый', 'Средний', 'Крупный')
        for i in range(3):
            c = checkTypeGab[i]
            if c == type_Gab:
                global w_Rec
                w_Rec = wRec[i]

        for i in range(3):
            d = checkTypeGab[i]
            if d == type_Gab:
                global d2_st
                global d34_st
                global d56_st
                global d7_st
                global d8_st
                d2_st = d2_GOST[i]
                d34_st = d34_GOST[i]
                d56_st = d56_GOST[i]
                d7_st = d7_GOST[i]
                d8_st = d8_GOST[i]

        global d2_In_Row
        global d34_In_Row
        global d56_In_Row
        global d7_In_Row
        global d8_In_Row
        d2_In_Row = d2_st[::2]
        d34_In_Row = d34_st[::2]
        d56_In_Row = d56_st[::2]
        d7_In_Row = d7_st[::2]
        d8_In_Row = d8_st[::2]

    # Подбор стандартных внутренних диаметров
    def in_diametr(self, W, w, d_row, ro=1):
        d = 2 * sqrt(W / (ro * pi * w)) * 1000
        m = d
        for i in range(len(d_row)):
            delta = abs(d - d_row[i])
            if delta < m:
                m = delta
                d_St = int(d_row[i])
        return d_St

    # Обозначение труб по ГОСТу для вывода на интерфейс
    def gost_mark(self, d, d_GOST):
        for i in range(len(d_GOST)):
            if d == d_GOST[i]:
                d_gost = (d + 2 * d_GOST[i + 1], d_GOST[i + 1])
                return d_gost

    # Функция расчета скоростей
    def speed_flow(self, W, d, ro=1):
        w = 4 * W / (ro * pi * (d / 1000) ** 2)
        return w

    # Функции расчета Рейнольдса и коэффициентов сопротивления трения
    def num_re(self, d, w, kin_vis):
        Re = d / 1000 * w / kin_vis
        return Re

    def coeff_friction(self, d, l, re):
        lamda = 0.11 * l / d * (0.1 / d + 68 / re) ** 0.25
        return lamda

    # Функция и расчет коэффициентов сопротивления спиральных элементов
    def coeff_resist_se(self, lamda, d, n, N, pl, D4):
        dzeta_se = lamda + 0.5 * n + 1.4 + 1.1 + 0.9 * (N / pl) ** 2 * (d / D4) ** 4
        return dzeta_se

    # Функцмя получения КМС из массива
    def nearest_value(self, x, row):
        t = x
        for i in range(len(row)):
            delta = abs(x - row[i])
            if delta < t:
                t = delta
                value = i
        return value

    # Функции расчета потерь давления
    def pressure_loss_friction(self, lamda, ro, w):
        delta_p_f = lamda * ro * w ** 2 / 2 / 1000
        return delta_p_f

    def pressure_loss_resist(self, dzeta, ro, w):
        delta_p_r = dzeta * ro * w ** 2 / 2 / 1000
        return delta_p_r

    # Процесс расчета
    def calc_process(self):
        # Плотность и вязкость
        hs = HSDiag()
        visc = Visc()
        t_Av = (t_In + t_Out) / 2

        PhysChar_In = hs.props_tp(t_In, p_In * 1000)
        ro_In = 1 / PhysChar_In['v']
        KinVis_In = visc.kvisc_tp(t_In, p_In * 1000)

        PhysChar_Av = hs.props_tp(t_Av, p_In * 1000)
        ro_Av = 1 / PhysChar_Av['v']
        KinVis_Av = visc.kvisc_tp(t_Av, p_In * 1000)

        PhysChar_Out = hs.props_tp(t_Out, p_In * 1000)
        ro_Out = 1 / PhysChar_Out['v']
        KinVis_Out = visc.kvisc_tp(t_Out, p_In * 1000)

        # Расчет расходов
        global X_ok
        global X_op
        X_ok = X_Ok / 100
        X_op = X_Op / 100
        W1_ok_In = X_ok * Wpv * Config_SE[4] / (Num_Col * N_ok) / ro_In
        W1_kp_Av = Wpv * Config_SE[4] / (Num_Col * N_kp) / ro_Av
        W1_op_Out = X_op * Wpv * Config_SE[4] / (Num_Col * N_op) / ro_Out
        W2_In = Wpv / ro_In
        W2_Out = Wpv / ro_Out
        W3_In = Wpv / (0.5 * Num_Col) / ro_In
        W4_Av = Wpv / (0.5 * Num_Col) / ro_Av
        W4_Out = X_op * Wpv / (0.5 * Num_Col) / ro_Out
        W5_In = X_ok * Wpv / Num_Col / ro_In
        W6_In = X_ok * Wpv / Num_Col / ro_In
        W7_Out = X_op * Wpv / (0.5 * Num_Col) / ro_Out
        W8_Out = X_op * Wpv / ro_Out

        # Расчет диаметров и обозначение по ГОСТ
        d1 = Config_SE[1] - 2 * Config_SE[2]
        d2 = self.in_diametr(W2_In, w_Rec[0], d2_In_Row)
        d34 = self.in_diametr(W4_Av, w_Rec[1], d34_In_Row)
        d56 = self.in_diametr(W5_In, w_Rec[2], d56_In_Row)
        d7 = self.in_diametr(W7_Out, w_Rec[3], d7_In_Row)
        d8 = self.in_diametr(W8_Out, w_Rec[4], d8_In_Row)

        global d1_Gost
        global d2_Gost
        global d34_Gost
        global d56_Gost
        global d7_Gost
        global d8_Gost
        d1_Gost = (Config_SE[1], Config_SE[2])
        d2_Gost = self.gost_mark(d2, d2_st)
        d34_Gost = self.gost_mark(d34, d34_st)
        d56_Gost = self.gost_mark(d56, d56_st)
        d7_Gost = self.gost_mark(d7, d7_st)
        d8_Gost = self.gost_mark(d8, d8_st)

        # Расчет скоростей
        w1_ok_In = self.speed_flow(W1_ok_In, d1)
        w1_kp_Av = self.speed_flow(W1_kp_Av, d1)
        w1_op_Out = self.speed_flow(W1_op_Out, d1)
        w2_In = self.speed_flow(W2_In, d2)
        w2_Out = self.speed_flow(W2_Out, d2)
        w3_In = self.speed_flow(W3_In, d34)
        w4_Av = self.speed_flow(W4_Av, d34)
        w4_Out = self.speed_flow(W4_Out, d34)
        w6_In = self.speed_flow(W6_In, d56)
        w7_Out = self.speed_flow(W7_Out, d7)
        w8_Out = self.speed_flow(W8_Out, d8)

        # Расчет длин
        global L2
        global L3
        global L4
        global L5
        global L6
        global L7
        global L8
        if Num_Col == 4:
            Z = 0.35
            Dk = 2.414 * Config_SE[7] + 2 * 0.05
            L6 = round(pi / 4 * (Dk - d34_Gost[0] / 1000 - 2 * 0.02) - d34_Gost[0] / 1000 - d56_Gost[0] / 1000 + 0.4, 2)
            L7 = round(0.6 * Dk, 2)
        else:
            Z = 0.6
            Dk = 3 * Config_SE[7] + 2 * 0.05
            L6 = round(pi / 9 * (Dk - d34_Gost[0] / 1000 - 2 * 0.02) + 0.4, 2)
            L7 = round(0.75 * Dk, 2)
        if type_Gab == 'Малый':
            L2 = 0.75
        elif type_Gab == 'Средний':
            L2 = 1.25
        else:
            L2 = 1.75
        H_SE = (N_ok + N_kp + N_op) * Config_SE[1] / 1000 + 0.006 * (N_ok + N_kp + N_op - 3) + Z
        L3 = round(0.89 * Dk, 2)
        L4 = round(1.15 * H_SE, 2)
        L8 = L4
        L5 = 0.5

        # Расчет чисел Рейнольдса
        Re1_ok_In = self.num_re(d1, w1_ok_In, KinVis_In)
        Re1_kp_Av = self.num_re(d1, w1_kp_Av, KinVis_Av)
        Re1_op_Out = self.num_re(d1, w1_op_Out, KinVis_Out)
        Re2_In = self.num_re(d2, w2_In, KinVis_In)
        Re2_Out = self.num_re(d2, w2_Out, KinVis_Out)
        Re3_In = self.num_re(d34, w3_In, KinVis_In)
        Re4_Av = self.num_re(d34, w4_Av, KinVis_Av)
        Re4_Out = self.num_re(d34, w4_Out, KinVis_Out)
        Re6_In = self.num_re(d56, w6_In, KinVis_In)
        Re7_Out = self.num_re(d7, w7_Out, KinVis_Out)
        Re8_Out = self.num_re(d8, w8_Out, KinVis_Out)

        # Расчет коэффициентов трения
        Lambda1_ok_In = self.coeff_friction(d1, Config_SE[6] * 1000, Re1_ok_In)
        Lambda1_kp_Av = self.coeff_friction(d1, Config_SE[6] * 1000, Re1_kp_Av)
        Lambda1_op_Out = self.coeff_friction(d1, Config_SE[6] * 1000, Re1_op_Out)
        Lambda2_In = self.coeff_friction(d2, L2 * 1000, Re2_In)
        Lambda2_Out = self.coeff_friction(d2, L2 * 1000, Re2_Out)
        Lambda3_In = self.coeff_friction(d34, L3 * 1000, Re3_In)
        Lambda4_Av = self.coeff_friction(d34, 0.65 * L4 * 1000, Re4_Av)
        Lambda4_Out = self.coeff_friction(d34, 0.35 * L4 * 1000, Re4_Out)
        Lambda6_In = self.coeff_friction(d56, L6 * 1000, Re6_In)
        Lambda7_Out = self.coeff_friction(d7, L7 * 1000, Re7_Out)
        Lambda8_Out = self.coeff_friction(d8, L8 * 1000, Re8_Out)

        # Расчет коэффициентов сопротивления спиральных элементов
        Dzeta_SE_ok = self.coeff_resist_se(Lambda1_ok_In, d1, Config_SE[5], N_ok, Config_SE[4], d34)
        Dzeta_SE_kp = self.coeff_resist_se(Lambda1_kp_Av, d1, Config_SE[5], N_kp, Config_SE[4], d34)
        Dzeta_SE_op = self.coeff_resist_se(Lambda1_op_Out, d1, Config_SE[5], N_op, Config_SE[4], d34)

        # Расчет потерь давления в зонах
        Delta_p_ok = round(self.pressure_loss_resist(Dzeta_SE_ok, ro_In, w1_ok_In), 2)
        Delta_p_kp = round(self.pressure_loss_resist(Dzeta_SE_kp, ro_Av, w1_kp_Av), 2)
        Delta_p_op = round(self.pressure_loss_resist(Dzeta_SE_op, ro_Out, w1_op_Out), 2)

        # Расчет КМС
        Dzeta_1 = 0.2639 * (w3_In / w2_In) ** 2 + 0.1144 * (w3_In / w2_In) + 0.9253
        Dzeta_2 = 0.256 + 14.175 * Lambda3_In * d34 / (L3 * 1000)
        Dzeta_3 = 0.11 + 4.725 * Lambda3_In * d34 / (L3 * 1000)
        Dzeta_4 = 1.58
        Dzeta_5 = 0.8
        Dzeta_6 = 1.58
        Dzeta_7 = 0.1 + 4.2 * Lambda7_Out * d7 / (L7 * 1000)
        if Num_Col == 4:
            Dzeta_8 = -91.667 * (d7 / d8) ** 6 + 167.5 * (d7 / d8) ** 4 - 102.83 * (d7 / d8) ** 2 + 23
        else:
            Dzeta_8 = 1.1
        Dzeta_9 = 0.132 + 7.1 * Lambda8_Out * d8 / (L8 * 1000)

        # Расчет КМС10
        x = (d8 / d2) ** 2
        y = X_op / (1 - X_op)
        dd = self.nearest_value(x, dd82)
        WW = self.nearest_value(y, WW28)
        f = dW[dd]
        Dzeta_10 = f[WW]

        # Расчет потерь на трение и МС
        Delta_p_2_In_f = self.pressure_loss_friction(Lambda2_In, ro_In, w2_In)
        Delta_p_2_Out_f = self.pressure_loss_friction(Lambda2_Out, ro_Out, w2_Out)
        Delta_p_3_In_f = self.pressure_loss_friction(Lambda3_In, ro_In, w3_In)
        Delta_p_4_Av_f = self.pressure_loss_friction(Lambda4_Av, ro_Av, w4_Av)
        Delta_p_4_Out_f = self.pressure_loss_friction(Lambda4_Out, ro_Out, w4_Out)
        Delta_p_6_In_f = self.pressure_loss_friction(Lambda6_In, ro_In, w6_In)
        Delta_p_7_Out_f = self.pressure_loss_friction(Lambda7_Out, ro_Out, w7_Out)
        Delta_p_8_Out_f = self.pressure_loss_friction(Lambda8_Out, ro_Out, w8_Out)
        Delta_p_1_In_r = self.pressure_loss_resist(Dzeta_1, ro_In, w2_In)
        Delta_p_2_In_r = self.pressure_loss_resist(Dzeta_2, ro_In, w3_In)
        Delta_p_3_In_r = self.pressure_loss_resist(Dzeta_3, ro_In, w3_In)
        Delta_p_4_In_r = self.pressure_loss_resist(Dzeta_4, ro_In, w6_In)
        Delta_p_5_In_r = self.pressure_loss_resist(Dzeta_5, ro_In, w6_In)
        Delta_p_6_Out_r = self.pressure_loss_resist(Dzeta_6, ro_Out, w4_Out)
        Delta_p_7_Out_r = self.pressure_loss_resist(Dzeta_7, ro_Out, w7_Out)
        Delta_p_8_Out_r = self.pressure_loss_resist(Dzeta_8, ro_Out, w7_Out)
        Delta_p_9_Out_r = self.pressure_loss_resist(Dzeta_9, ro_Out, w8_Out)
        Delta_p_10_Out_r = self.pressure_loss_resist(Dzeta_10, ro_Out, w8_Out)

        # Суммарные потери в спиралях
        global Delta_p_se
        global Delta_p_r
        global Delta_p_f
        global Delta_p_abs
        global Delta_p_comp
        global Delta_p_comp_se
        global Delta_p_comp_r
        global Delta_p_comp_f
        Delta_p_se = round(Delta_p_ok + Delta_p_kp + Delta_p_op, 1)

        # Результат и его вывод с рекомендациями по полной методке
        Delta_p_r = round(
            Delta_p_1_In_r + Delta_p_2_In_r + Delta_p_3_In_r + Delta_p_4_In_r + Delta_p_5_In_r + Delta_p_6_Out_r
            + Delta_p_7_Out_r + Delta_p_8_Out_r + Delta_p_9_Out_r + Delta_p_10_Out_r, 1)
        Delta_p_f = round(Delta_p_2_In_f + Delta_p_2_Out_f + Delta_p_3_In_f + Delta_p_4_Av_f + Delta_p_4_Out_f
                          + Delta_p_6_In_f + Delta_p_7_Out_f + Delta_p_8_Out_f, 1)
        Delta_p_abs = round(Delta_p_se + Delta_p_r + Delta_p_f, 1)
        Delta_p_comp = round(Delta_p_abs / p_In * 100, 2)
        Delta_p_comp_se = round(Delta_p_se / Delta_p_abs * 100, 2)
        Delta_p_comp_r = round(Delta_p_r / Delta_p_abs * 100, 2)
        Delta_p_comp_f = round(Delta_p_f / Delta_p_abs * 100, 2)

        # Результаты для упрощенной методики
        if Metod == 'Упрощенный':
            Delta_p_abs = round(1.1 * Delta_p_se, 1)
            Delta_p_comp = round(Delta_p_abs / p_In * 100, 2)

    # Отображение результатов
    def show_results(self):
        global ID
        ID = (Wpv, N_ok, N_kp, N_op, X_ok, X_op, t_In, t_Out, p_In, Metod)
        self.pushButton_25.setDisabled(False)
        if Metod == 'Полный':
            self.label_9.setText(str(d1_Gost[0]))
            self.label_20.setText(str(d1_Gost[1]))
            self.label_24.setText(str(d2_Gost[0]))
            self.label_26.setText(str(d2_Gost[1]))
            self.label_30.setText(str(d34_Gost[0]))
            self.label_32.setText(str(d34_Gost[1]))
            self.label_36.setText(str(d34_Gost[0]))
            self.label_38.setText(str(d34_Gost[1]))
            self.label_42.setText(str(d56_Gost[0]))
            self.label_44.setText(str(d56_Gost[1]))
            self.label_48.setText(str(d56_Gost[0]))
            self.label_50.setText(str(d56_Gost[1]))
            self.label_54.setText(str(d7_Gost[0]))
            self.label_56.setText(str(d7_Gost[1]))
            self.label_60.setText(str(d8_Gost[0]))
            self.label_62.setText(str(d8_Gost[1]))
            self.label_22.setText(str(Config_SE[6]))
            self.label_28.setText(str(L2))
            self.label_34.setText(str(L3))
            self.label_40.setText(str(L4))
            self.label_46.setText(str(L5))
            self.label_52.setText(str(L6))
            self.label_58.setText(str(L7))
            self.label_64.setText(str(L8))
            self.label_66.setText(str(Delta_p_abs))
            self.label_69.setText(str(Delta_p_comp))
            self.label_75.setText(str(Delta_p_se))
            self.label_76.setText(str(Delta_p_r))
            self.label_77.setText(str(Delta_p_f))
            self.label_70.setText(str(Delta_p_comp_se))
            self.label_71.setText(str(Delta_p_comp_r))
            self.label_72.setText(str(Delta_p_comp_f))

            # Вывод рекомендаций
            if Delta_p_abs < Config_Limits[5]:
                self.label_67.setText(
                    'Потери давления ниже диапазона допустимых значений для данной компоновки.' + '\n' +
                    'Необходимо уменьшить число рядов спиралей в зонах, увеличить доли расхода' + '\n' +
                    'воды, направляемой в зоны ОК и ОП или выбрать другой тип компоновки.')
            elif Delta_p_abs > Config_Limits[6]:
                self.label_67.setText(
                    'Потери давления выше диапазона допустимых значений для данной компоновки.' + '\n' +
                    'Необходимо увеличить число рядов спиралей в зонах, уменьшить доли расхода' + '\n' +
                    'воды, направляемой в зоны ОК и ОП или выбрать другой тип компоновки.')
            else:
                self.label_67.setText(
                    'Гидравлический режим выбранной компоновки подогревателя ' + '\n' + 'удовлетворительный.' + '\n')
        else:
            self.label_9.setText(str(d1_Gost[0]))
            self.label_20.setText(str(d1_Gost[1]))
            self.label_24.setText(str('―'))
            self.label_26.setText(str('―'))
            self.label_30.setText(str(d34_Gost[0]))
            self.label_32.setText(str(d34_Gost[1]))
            self.label_36.setText(str(d34_Gost[0]))
            self.label_38.setText(str(d34_Gost[1]))
            self.label_42.setText(str('―'))
            self.label_44.setText(str('―'))
            self.label_48.setText(str('―'))
            self.label_50.setText(str('―'))
            self.label_54.setText(str('―'))
            self.label_56.setText(str('―'))
            self.label_60.setText(str('―'))
            self.label_62.setText(str('―'))
            self.label_22.setText(str('―'))
            self.label_28.setText(str('―'))
            self.label_34.setText(str('―'))
            self.label_40.setText(str('―'))
            self.label_46.setText(str('―'))
            self.label_52.setText(str('―'))
            self.label_58.setText(str('―'))
            self.label_64.setText(str('―'))
            self.label_66.setText(str(Delta_p_abs))
            self.label_69.setText(str(Delta_p_comp))
            self.label_75.setText(str(Delta_p_se))
            self.label_76.setText(str('―'))
            self.label_77.setText(str('―'))
            self.label_70.setText(str('―'))
            self.label_71.setText(str('―'))
            self.label_72.setText(str('―'))

            # Вывод рекомендаций
            if Delta_p_abs < Config_Limits[5]:
                self.label_67.setText(
                    'Потери давления ниже диапазона допустимых значений для данной компоновки.' + '\n' +
                    'Необходимо уменьшить число рядов спиралей в зонах, увеличить доли расхода' + '\n' +
                    'воды, направляемой в зоны ОК и ОП или выбрать другой тип компоновки.')
            elif Delta_p_abs > Config_Limits[6]:
                self.label_67.setText(
                    'Потери давления выше диапазона допустимых значений для данной компоновки.' + '\n' +
                    'Необходимо увеличить число рядов спиралей в зонах, уменьшить доли расхода' + '\n' +
                    'воды, направляемой в зоны ОК и ОП или выбрать другой тип компоновки.')
            else:
                self.label_67.setText(
                    'Гидравлический режим выбранной компоновки подогревателя ' + '\n' + 'удовлетворительный.' + '\n')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
