# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddingData.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NameSelection = QtWidgets.QComboBox(self.centralwidget)
        self.NameSelection.setGeometry(QtCore.QRect(20, 40, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.NameSelection.setFont(font)
        self.NameSelection.setObjectName("NameSelection")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.AddingDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddingDataButton.setGeometry(QtCore.QRect(242, 371, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.AddingDataButton.setFont(font)
        self.AddingDataButton.setObjectName("AddingDataButton")
        self.NumberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NumberEdit.setGeometry(QtCore.QRect(20, 140, 121, 31))
        self.NumberEdit.setObjectName("NumberEdit")
        self.DateEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DateEdit.setGeometry(QtCore.QRect(20, 250, 131, 31))
        self.DateEdit.setObjectName("DateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление данных"))
        self.label.setText(_translate("MainWindow", "Название:"))
        self.label_2.setText(_translate("MainWindow", "Количество:"))
        self.label_4.setText(_translate("MainWindow", "Годен до:"))
        self.AddingDataButton.setText(_translate("MainWindow", "Добавить"))
