import sqlite3
import csv
from datetime import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QPushButton, QApplication, QVBoxLayout, \
    QWidget, QInputDialog, QMessageBox


class Ui_MainWindow_NewNumberForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 291)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.DoneButton.setGeometry(QtCore.QRect(150, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DoneButton.setFont(font)
        self.DoneButton.setObjectName("DoneButton")
        self.NewNumberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NewNumberEdit.setGeometry(QtCore.QRect(30, 70, 211, 41))
        self.NewNumberEdit.setObjectName("NewNumberEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменение количества"))
        self.label.setText(_translate("MainWindow", "Изменить количество:"))
        self.DoneButton.setText(_translate("MainWindow", "Готово"))


class Ui_MainWindow_AddingData(object):
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


class Ui_MainWindow_MainForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 783)
        MainWindow.setMinimumSize(QtCore.QSize(1011, 783))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(60, 40, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.RequiredTable = QtWidgets.QTableWidget(self.tab)
        self.RequiredTable.setGeometry(QtCore.QRect(60, 130, 863, 360))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.RequiredTable.setFont(font)
        self.RequiredTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.RequiredTable.setObjectName("RequiredTable")
        self.RequiredTable.setColumnCount(0)
        self.RequiredTable.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.CurrentDateLabel = QtWidgets.QLabel(self.tab_2)
        self.CurrentDateLabel.setGeometry(QtCore.QRect(20, 30, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CurrentDateLabel.setFont(font)
        self.CurrentDateLabel.setText("")
        self.CurrentDateLabel.setObjectName("CurrentDateLabel")
        self.ReportTable1 = QtWidgets.QTableWidget(self.tab_2)
        self.ReportTable1.setGeometry(QtCore.QRect(20, 139, 501, 421))
        self.ReportTable1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ReportTable1.setObjectName("ReportTable1")
        self.ReportTable1.setColumnCount(0)
        self.ReportTable1.setRowCount(0)
        self.ReportTable2 = QtWidgets.QTableWidget(self.tab_2)
        self.ReportTable2.setGeometry(QtCore.QRect(598, 139, 360, 421))
        self.ReportTable2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ReportTable2.setObjectName("ReportTable2")
        self.ReportTable2.setColumnCount(0)
        self.ReportTable2.setRowCount(0)
        self.CurrentDateLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.CurrentDateLabel_2.setGeometry(QtCore.QRect(20, 100, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CurrentDateLabel_2.setFont(font)
        self.CurrentDateLabel_2.setObjectName("CurrentDateLabel_2")
        self.CurrentDateLabel_3 = QtWidgets.QLabel(self.tab_2)
        self.CurrentDateLabel_3.setGeometry(QtCore.QRect(600, 100, 350, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CurrentDateLabel_3.setFont(font)
        self.CurrentDateLabel_3.setObjectName("CurrentDateLabel_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CreateKitButton = QtWidgets.QPushButton(self.centralwidget)
        self.CreateKitButton.setObjectName("CreateKitButton")
        self.horizontalLayout_2.addWidget(self.CreateKitButton)
        self.DeleteKitButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteKitButton.setObjectName("DeleteKitButton")
        self.horizontalLayout_2.addWidget(self.DeleteKitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.ReportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReportButton.setObjectName("ReportButton")
        self.verticalLayout.addWidget(self.ReportButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElKit"))
        self.label.setText(_translate("MainWindow", "Требования к комплектации аптечек:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Справочник"))
        self.CurrentDateLabel_2.setText(_translate("MainWindow", "Недостающие изделия:"))
        self.CurrentDateLabel_3.setText(_translate("MainWindow", "Изделия с истекшим сроком годности:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Отчет"))
        self.CreateKitButton.setText(_translate("MainWindow", "Создать аптечку"))
        self.DeleteKitButton.setText(_translate("MainWindow", "Удалить аптечку"))
        self.ReportButton.setText(_translate("MainWindow", "Сформировать отчет"))


class Ui_MainWindow_WelcomeForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 783)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setEnabled(True)
        self.NextButton.setGeometry(QtCore.QRect(420, 650, 171, 41))
        self.NextButton.setMaximumSize(QtCore.QSize(16777215, 16777212))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.NextButton.setFont(font)
        self.NextButton.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border: 1px solid rgb(204, 204, 204);")
        self.NextButton.setObjectName("NextButton")
        self.ImgL1 = QtWidgets.QLabel(self.centralwidget)
        self.ImgL1.setEnabled(True)
        self.ImgL1.setGeometry(QtCore.QRect(430, 110, 151, 129))
        self.ImgL1.setMinimumSize(QtCore.QSize(151, 129))
        self.ImgL1.setMaximumSize(QtCore.QSize(151, 16777212))
        self.ImgL1.setObjectName("ImgL1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(320, 20, 371, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777212))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 331, 51))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.label_3.setObjectName("label_3")
        self.ImgL2 = QtWidgets.QLabel(self.centralwidget)
        self.ImgL2.setEnabled(True)
        self.ImgL2.setGeometry(QtCore.QRect(70, 350, 21, 21))
        self.ImgL2.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.ImgL2.setObjectName("ImgL2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setEnabled(True)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 340, 441, 80))
        self.verticalLayoutWidget.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setEnabled(True)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setEnabled(True)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setEnabled(True)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 450, 535, 41))
        self.verticalLayoutWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setEnabled(True)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.ImgL3 = QtWidgets.QLabel(self.centralwidget)
        self.ImgL3.setEnabled(True)
        self.ImgL3.setGeometry(QtCore.QRect(70, 460, 21, 21))
        self.ImgL3.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.ImgL3.setObjectName("ImgL3")
        self.ImgL4 = QtWidgets.QLabel(self.centralwidget)
        self.ImgL4.setEnabled(True)
        self.ImgL4.setGeometry(QtCore.QRect(70, 530, 21, 21))
        self.ImgL4.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.ImgL4.setObjectName("ImgL4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setEnabled(True)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(100, 520, 706, 41))
        self.verticalLayoutWidget_3.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setEnabled(True)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElKit"))
        self.centralwidget.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.NextButton.setText(_translate("MainWindow", "Продолжить"))
        self.ImgL1.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/ElKit/k.png\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать в ElKit!"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:24pt;\">В этом приложении "
                                        "можно:</span></p></body></html>"))
        self.ImgL2.setText(_translate("MainWindow",
                                      "<html><head/><body><p><img src=\":/newPrefix/ElKit/cross.png\"/></p></body"
                                      "></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Отслеживать наличие "
                                        "медецинских изделий в</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">аптечках "
                                        "общественного транспорта</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Следить за сроком "
                                        "годности медецинских изделий в аптечках</span></p></body></html>"))
        self.ImgL3.setText(_translate("MainWindow",
                                      "<html><head/><body><p><img src=\":/newPrefix/ElKit/cross.png\"/></p></body"
                                      "></html>"))
        self.ImgL4.setText(_translate("MainWindow",
                                      "<html><head/><body><p><img src=\":/newPrefix/ElKit/cross.png\"/></p></body"
                                      "></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Просматривать "
                                        "информацию о требованиях к содержанию аптечек в "
                                        "справочнике</span></p></body></html>"))


class WelcomeForm(QMainWindow, Ui_MainWindow_WelcomeForm):  # Приветственная форма
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.NextButton.clicked.connect(self.open_main_form)

        qpixmap1 = QPixmap('k.png')
        qpixmap2 = QPixmap('cross.png')
        self.ImgL1.setPixmap(qpixmap1)
        self.ImgL2.setPixmap(qpixmap2)
        self.ImgL3.setPixmap(qpixmap2)
        self.ImgL4.setPixmap(qpixmap2)

    def open_main_form(self):  # Переход к следующей (основной) форме
        self.main_form = MainForm(self)
        self.main_form.show()
        self.hide()


class MainForm(QMainWindow, Ui_MainWindow_MainForm):  # Основная форма
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.CreateKitButton.clicked.connect(self.create_kit)
        self.DeleteKitButton.clicked.connect(self.delete_kit)
        self.ReportButton.clicked.connect(self.make_report)
        MainForm.Tab = self.tabWidget
        MainForm.Index = self.tabWidget.currentIndex()

        MainForm.con = sqlite3.connect("ElectronicKit.db")
        MainForm.cur = MainForm.con.cursor()
        req = f"SELECT Name, RequiredNumber, Unit FROM RequiredMedicalProducts"
        result = MainForm.cur.execute(req).fetchall()
        self.RequiredTable.setColumnCount(3)
        self.RequiredTable.setRowCount(len(result))
        self.RequiredTable.setHorizontalHeaderLabels(["Название", "Количество", "Единицы измерения"])
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.RequiredTable.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.RequiredTable.resizeColumnsToContents()

    def create_kit(self):  # Создание новой аптечки
        name, ok_pressed = QInputDialog.getText(self, "Создание аптечки",
                                                "Название аптечки:")
        if ok_pressed:
            MainForm.Tab.addTab(NewKitTab(), name)

            MainForm.cur.execute(f'''CREATE TABLE IF NOT EXISTS Table{MainForm.Tab.count() - 1}
                         ("ID"	INTEGER NOT NULL UNIQUE, "Name"	TEXT NOT NULL, "Number"	INTEGER NOT NULL,
                          "Unit"	TEXT NOT NULL, "ExpDate"	TEXT NOT NULL, PRIMARY KEY("ID" AUTOINCREMENT),
                           FOREIGN KEY("Unit") REFERENCES "RequiredMedicalProducts"("Unit"), FOREIGN KEY("Name")
                            REFERENCES "RequiredMedicalProducts"("Name"))''')

    def delete_kit(self):  # Удаление аптечки
        if self.tabWidget.currentIndex() != 0 and self.tabWidget.currentIndex() != 1:
            button_reply = QMessageBox.question(self, 'PyQt5 message', "Вы действительно хотите удалить аптечку?",
                                                QMessageBox.Yes | QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                if self.tabWidget.currentIndex() != 0 and self.tabWidget.currentIndex() != 1:
                    MainForm.DelIndex = self.tabWidget.currentIndex()
                    self.tabWidget.removeTab(MainForm.DelIndex)
                    MainForm.cur.execute(f"DROP TABLE Table{MainForm.DelIndex}")
                    if MainForm.Tab.count() != 2:
                        for i in range(MainForm.DelIndex + 1, MainForm.Tab.count() + 1):
                            MainForm.cur.execute(f"ALTER TABLE Table{i} RENAME TO Table{i - 1}")
                    MainForm.con.commit()

    def make_report(self):  # Формирование отчета
        if MainForm.Tab.count() > 2:
            MainForm.cur.execute('''CREATE TABLE IF NOT EXISTS ReportTable1
                                 ("ID"	INTEGER NOT NULL UNIQUE, "KitName"	TEXT NOT NULL, "Name"	TEXT NOT NULL,
                                  "Number"	TEXT NOT NULL, PRIMARY KEY("ID" AUTOINCREMENT))''')
            MainForm.cur.execute('DELETE FROM ReportTable1')
            MainForm.cur.execute('''CREATE TABLE IF NOT EXISTS ReportTable2
                                         ("KitName"	TEXT NOT NULL, "№"	INTEGER NOT NULL,
                                          "Name" TEXT NOT NULL)''')
            MainForm.cur.execute('DELETE FROM ReportTable2')
            self.ReportTable1.setColumnCount(3)
            self.ReportTable1.setRowCount(MainForm.Tab.count() - 2)
            self.ReportTable1.setHorizontalHeaderLabels(["Аптечка", "Изделие", "Кол-во"])
            self.ReportTable1.setColumnWidth(0, 57)
            self.ReportTable1.setColumnWidth(1, 360)
            self.ReportTable1.setColumnWidth(2, 60)

            self.ReportTable2.setColumnCount(3)
            self.ReportTable2.setRowCount(MainForm.Tab.count() - 2)
            self.ReportTable2.setHorizontalHeaderLabels(["Аптечка", "№", "Изделие"])
            self.ReportTable2.setColumnWidth(0, 60)
            self.ReportTable2.setColumnWidth(1, 10)
            self.ReportTable2.setColumnWidth(2, 279)

            for k in range(MainForm.Tab.count() - 2):
                for q in range(1,
                               MainForm.cur.execute("SELECT COUNT(*) FROM RequiredMedicalProducts").fetchone()[0] + 1):
                    number_list = [0]
                    res = MainForm.cur.execute(f"""SELECT Number FROM Table{k + 2} 
                    WHERE Name like (SELECT Name FROM RequiredMedicalProducts WHERE ID = {q})""").fetchall()
                    for n in range(len(res)):
                        number_list.append(res[n][0])
                    number = sum(number_list)
                    req_number = MainForm.cur.execute(f"SELECT RequiredNumber"
                                                      f" FROM RequiredMedicalProducts WHERE ID = {q}").fetchone()[0]
                    if number < req_number:
                        b = MainForm.cur.execute(f"SELECT Name"
                                                 f" FROM RequiredMedicalProducts WHERE ID = {q}").fetchone()[0]
                        a = self.tabWidget.tabText(k + 2)
                        c = str(req_number - number) + ' ' + str(MainForm.cur.execute(f"SELECT Unit FROM"
                                                                                      f" RequiredMedicalProducts WHERE"
                                                                                      f" ID = {q}").fetchone()[0])
                        MainForm.cur.execute(f"INSERT INTO ReportTable1 (KitName, Name, Number)"
                                             f" VALUES ('{a}', '{b}', '{c}')")
                        MainForm.con.commit()
            for k in range(MainForm.Tab.count() - 2):
                for q in range(MainForm.cur.execute(f"SELECT COUNT(*) FROM Table{k + 2}").fetchone()[0]):
                    date = MainForm.cur.execute(f"SELECT ExpDate FROM Table{k + 2} WHERE ID ="
                                                f" (SELECT ID FROM Table{k + 2} LIMIT 1 OFFSET {q})").fetchone()[0]
                    current_date = datetime.now()
                    date1 = date.split('.')
                    exp_date = datetime(year=int(date1[2]), month=int(date1[1]), day=int(date1[0]))
                    diff = exp_date - current_date
                    if diff.days < 0:
                        a = self.tabWidget.tabText(k + 2)
                        b = q + 1
                        c = MainForm.cur.execute(f"SELECT Name FROM Table{k + 2} WHERE ID ="
                                                 f" (SELECT ID FROM Table{k + 2} LIMIT 1 OFFSET {q})").fetchone()[0]
                        MainForm.cur.execute(f"INSERT INTO ReportTable2 (KitName, №, Name)"
                                             f" VALUES ('{a}', '{b}', '{c}')")
                        MainForm.con.commit()

                req = f"SELECT KitName, Name, Number FROM ReportTable1"
                result = MainForm.cur.execute(req).fetchall()
                self.ReportTable1.setRowCount(len(result))
                for i, row in enumerate(result):
                    for j, elem in enumerate(row):
                        self.ReportTable1.setItem(
                            i, j, QTableWidgetItem(str(elem)))

                req = f"SELECT KitName, №, Name FROM ReportTable2"
                result = MainForm.cur.execute(req).fetchall()
                self.ReportTable2.setRowCount(len(result))
                for i, row in enumerate(result):
                    for j, elem in enumerate(row):
                        self.ReportTable2.setItem(
                            i, j, QTableWidgetItem(str(elem)))

            current_datetime = datetime.now()
            self.CurrentDateLabel.setText(f'Отчет сформирован'
                                          f' {current_datetime.date().strftime("%d.%m.%Y")}'
                                          f' в {current_datetime.time().strftime("%H:%M")}')
            with open('report1.csv', 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                writer.writerow(
                    [self.ReportTable1.horizontalHeaderItem(i).text()
                     for i in range(self.ReportTable1.columnCount())])
                for i in range(self.ReportTable1.rowCount()):
                    row = []
                    for j in range(self.ReportTable1.columnCount()):
                        item = self.ReportTable1.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)

            with open('report2.csv', 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                writer.writerow(
                    [self.ReportTable2.horizontalHeaderItem(i).text()
                     for i in range(self.ReportTable2.columnCount())])
                for i in range(self.ReportTable2.rowCount()):
                    row = []
                    for j in range(self.ReportTable2.columnCount()):
                        item = self.ReportTable2.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)




    def closeEvent(self, event):  # Закрытие приложения
        for i in range(1, MainForm.Tab.count() - 1):
            MainForm.cur.execute(f"DROP TABLE Table{i + 1}")
        MainForm.con.close()


class AddingDataForm(QMainWindow, Ui_MainWindow_AddingData):  # Форма добавления данных в аптечку
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.AddingDataButton.clicked.connect(self.add_data)
        result1 = MainForm.cur.execute("SELECT Name FROM RequiredMedicalProducts")
        for e in result1:
            self.NameSelection.addItem(e[0])

    def add_data(self):  # Добавление данных
        num = self.NumberEdit.text()
        date = self.DateEdit.text()
        if not num.isdigit():
            self.statusBar().showMessage(
                'Введите корректное количество в формате целого числа.')
            return
        date_string = date
        date_format = "%d.%m.%Y"
        try:
            datetime.strptime(date_string, date_format)
        except ValueError:
            self.statusBar().showMessage('Введите корректную дату в формате дд.мм.гггг.')
            return
        self.statusBar().showMessage('')
        a = self.NameSelection.currentText()
        b = self.NumberEdit.text()
        d = self.DateEdit.text()
        r = f"SELECT Unit FROM RequiredMedicalProducts WHERE Name in ('{a}')"
        c = MainForm.cur.execute(r).fetchall()
        MainForm.cur.execute(f"INSERT INTO Table{MainForm.Tab.currentIndex()} (Name, Number, Unit, ExpDate)"
                             f" VALUES ('{a}', {b}, '{c[0][0]}', '{d}')")
        MainForm.con.commit()
        page = MainForm.Tab.widget(MainForm.Tab.currentIndex())
        self.tablewidget = page.findChild(QTableWidget)
        req = f"SELECT Name, Number, Unit, ExpDate FROM Table{MainForm.Tab.currentIndex()}"
        result = MainForm.cur.execute(req).fetchall()
        self.tablewidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tablewidget.setItem(
                    i, j, QTableWidgetItem(str(elem), Qt.ItemIsSelectable | Qt.ItemIsEnabled))
        self.tablewidget.resizeColumnsToContents()
        self.tablewidget.setColumnWidth(0, 480)

        self.hide()


class NewKitTab(QWidget):  # Форма-макет для новой вкладки с аптечкой
    def __init__(self):
        super().__init__()
        self.Table = QTableWidget(self)
        self.Table.setEditTriggers(self.Table.NoEditTriggers)
        self.Table.setColumnCount(4)
        self.Table.setHorizontalHeaderLabels(["Название", "Количество", "Единицы измерения", "Годен до"])
        self.Table.resizeColumnsToContents()
        self.Table.setFixedSize(900, 400)
        self.Table.setFont(QFont('AppleSystemUIFont', 18))
        self.Table.resizeColumnsToContents()
        self.Table.setColumnWidth(0, 480)
        self.Table.setColumnWidth(3, 110)

        self.AddDataButton = QPushButton('Добавить данные', self)
        self.AddDataButton.clicked.connect(self.add)

        self.EditDataButton = QPushButton('Изменить количество', self)
        self.EditDataButton.clicked.connect(self.edit)

        self.DeleteDataButton = QPushButton('Удалить данные', self)
        self.DeleteDataButton.clicked.connect(self.delete)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.AddDataButton)
        self.verticalLayout.addWidget(self.EditDataButton)
        self.verticalLayout.addWidget(self.DeleteDataButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.Table)
        vbox.addLayout(self.verticalLayout)

        self.setLayout(vbox)

    def add(self):  # Добавление данных в аптечку
        self.addData_form = AddingDataForm(self)
        self.addData_form.show()

    def edit(self):  # Редактирование данных аптечки
        NewKitTab.index = self.Table.currentRow()
        self.EditNumber_form = EditingNumberForm(self)
        self.EditNumber_form.show()

    def delete(self):  # Удаление данных из аптечки
        index = self.Table.currentRow()
        button_reply = QMessageBox.question(self, 'PyQt5 message', "Вы действительно хотите удалить данные?",
                                            QMessageBox.Yes | QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            MainForm.cur.execute(
                f"DELETE FROM Table{MainForm.Tab.currentIndex()} WHERE ID = (SELECT ID FROM Table{MainForm.Tab.currentIndex()} LIMIT 1 OFFSET {index})")
            MainForm.con.commit()
            page = MainForm.Tab.widget(MainForm.Tab.currentIndex())
            self.tablewidget = page.findChild(QTableWidget)
            req = f"SELECT Name, Number, Unit, ExpDate FROM Table{MainForm.Tab.currentIndex()}"
            result = MainForm.cur.execute(req).fetchall()
            self.tablewidget.setRowCount(len(result))
            for i, row in enumerate(result):
                for j, elem in enumerate(row):
                    self.tablewidget.setItem(
                        i, j, QTableWidgetItem(str(elem), Qt.ItemIsSelectable | Qt.ItemIsEnabled))
            self.tablewidget.resizeColumnsToContents()
            self.tablewidget.setColumnWidth(0, 480)


class EditingNumberForm(QMainWindow, Ui_MainWindow_NewNumberForm):  # Форма редактирования данных
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.DoneButton.clicked.connect(self.set_new_number)

    def set_new_number(self):  # Редактирование данных
        new_num = self.NewNumberEdit.text()
        if not new_num.isdigit():
            self.statusBar().showMessage('Введите корректное количество в формате целого числа.')
            return
        self.statusBar().showMessage('')
        MainForm.cur.execute(
            f"UPDATE Table{MainForm.Tab.currentIndex()} SET Number = {new_num} "
            f"WHERE ID = (SELECT ID FROM Table{MainForm.Tab.currentIndex()} LIMIT 1 OFFSET {NewKitTab.index})")
        MainForm.con.commit()
        page = MainForm.Tab.widget(MainForm.Tab.currentIndex())
        self.tablewidget = page.findChild(QTableWidget)
        req = f"SELECT Name, Number, Unit, ExpDate FROM Table{MainForm.Tab.currentIndex()}"
        result = MainForm.cur.execute(req).fetchall()
        self.tablewidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tablewidget.setItem(
                    i, j, QTableWidgetItem(str(elem), Qt.ItemIsSelectable | Qt.ItemIsEnabled))
        self.tablewidget.resizeColumnsToContents()
        self.tablewidget.setColumnWidth(0, 480)
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WelcomeForm()
    ex.show()
    sys.exit(app.exec_())