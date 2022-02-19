# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import pexpect
import re
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets

import utils


child = pexpect.spawn('pm3')

child.expect('usb')

print(child.before.decode('utf-8'))

last_read_file = ""


class Ui_MainWindow(object):

    def read_card(self):
        global last_read_file
        child.sendline('hf mf autopwn')
        child.expect('pm3 -->')
        result = child.before.decode('utf-8')
        new_file_path = utils.analyze_result_files(result)
        if new_file_path:
            last_read_file = new_file_path
        print(result)
    
    def clone_card(self):
        global last_read_file
        if last_read_file:
            child.sendline(f'hf mf cload -f {last_read_file}')
            child.expect('pm3 -->')
            result = child.before.decode('utf-8')
            print(result)

    def move_result_files(self, string):
        eml_file = re.search(r'hf-mf-.*\.eml', string)
        if eml_file:
            eml_file = eml_file.group()
            return shutil.move(eml_file, "files")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 800)
        MainWindow.setMinimumSize(QtCore.QSize(480, 800))
        MainWindow.setMaximumSize(QtCore.QSize(480, 800))
        MainWindow.setStyleSheet("background-color: rgb(17, 25, 39);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 421, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_menu_vert_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_menu_vert_layout.setContentsMargins(0, 0, 0, 0)
        self.main_menu_vert_layout.setObjectName("main_menu_vert_layout")
        self.button_scan = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_scan.sizePolicy().hasHeightForWidth())
        self.button_scan.setSizePolicy(sizePolicy)
        self.button_scan.setMinimumSize(QtCore.QSize(0, 170))
        self.button_scan.setMaximumSize(QtCore.QSize(16777215, 170))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_scan.setFont(font)
        self.button_scan.setAutoFillBackground(True)
        self.button_scan.setStyleSheet("\n"
"background-color: rgb(255, 230, 0);")
        self.button_scan.setObjectName("button_scan")
        self.main_menu_vert_layout.addWidget(self.button_scan)
        self.button_clone = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clone.sizePolicy().hasHeightForWidth())
        self.button_clone.setSizePolicy(sizePolicy)
        self.button_clone.setMinimumSize(QtCore.QSize(0, 170))
        self.button_clone.setMaximumSize(QtCore.QSize(16777215, 170))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_clone.setFont(font)
        self.button_clone.setAutoFillBackground(True)
        self.button_clone.setStyleSheet("\n"
"background-color: rgb(255, 230, 0);")
        self.button_clone.setObjectName("button_clone")
        self.main_menu_vert_layout.addWidget(self.button_clone)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_scan.clicked.connect(self.read_card)
        self.button_clone.clicked.connect(self.clone_card)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_scan.setText(_translate("MainWindow", "READ CARD"))
        self.button_clone.setText(_translate("MainWindow", "CLONE CARD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
