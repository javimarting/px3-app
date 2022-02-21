# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app-gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 730)
        MainWindow.setMinimumSize(QtCore.QSize(480, 0))
        MainWindow.setStyleSheet("\n"
"background-color: rgb(3, 3, 40);\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("QPushButton {\n"
"background-color: rgb(33, 136, 145);\n"
"/*background-color: rgb(25, 145, 190);*/\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10;\n"
"font-size: 20pt;\n"
"}\n"
"QPushButton: hover {\n"
"background: rgb(28, 123, 130);\n"
"}\n"
"padding: 10pt;\n"
"\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.connectProxmarkPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectProxmarkPage.sizePolicy().hasHeightForWidth())
        self.connectProxmarkPage.setSizePolicy(sizePolicy)
        self.connectProxmarkPage.setObjectName("connectProxmarkPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.connectProxmarkPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pxmkappLabel = QtWidgets.QLabel(self.connectProxmarkPage)
        self.pxmkappLabel.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pxmkappLabel.setFont(font)
        self.pxmkappLabel.setStyleSheet("color: rgb(33, 136, 145);\n"
"border-radius: 10pt;\n"
"\n"
"")
        self.pxmkappLabel.setScaledContents(False)
        self.pxmkappLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pxmkappLabel.setObjectName("pxmkappLabel")
        self.verticalLayout_2.addWidget(self.pxmkappLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.connectProxmarkButton = QtWidgets.QPushButton(self.connectProxmarkPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectProxmarkButton.sizePolicy().hasHeightForWidth())
        self.connectProxmarkButton.setSizePolicy(sizePolicy)
        self.connectProxmarkButton.setMinimumSize(QtCore.QSize(0, 150))
        self.connectProxmarkButton.setMaximumSize(QtCore.QSize(600, 150))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(False)
        self.connectProxmarkButton.setFont(font)
        self.connectProxmarkButton.setAutoFillBackground(False)
        self.connectProxmarkButton.setStyleSheet("")
        self.connectProxmarkButton.setObjectName("connectProxmarkButton")
        self.verticalLayout_2.addWidget(self.connectProxmarkButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.connectProxmarkPage)
        self.mifarePage = QtWidgets.QWidget()
        self.mifarePage.setObjectName("mifarePage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.mifarePage)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.mifareStackedWidget = QtWidgets.QStackedWidget(self.mifarePage)
        self.mifareStackedWidget.setObjectName("mifareStackedWidget")
        self.mifareOptionsPage = QtWidgets.QWidget()
        self.mifareOptionsPage.setObjectName("mifareOptionsPage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.mifareOptionsPage)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.readMifareTagButton = QtWidgets.QPushButton(self.mifareOptionsPage)
        self.readMifareTagButton.setMinimumSize(QtCore.QSize(0, 80))
        self.readMifareTagButton.setObjectName("readMifareTagButton")
        self.verticalLayout_9.addWidget(self.readMifareTagButton)
        self.cloneMifareTagButton = QtWidgets.QPushButton(self.mifareOptionsPage)
        self.cloneMifareTagButton.setMinimumSize(QtCore.QSize(0, 80))
        self.cloneMifareTagButton.setObjectName("cloneMifareTagButton")
        self.verticalLayout_9.addWidget(self.cloneMifareTagButton)
        self.simulateMifareTagButton = QtWidgets.QPushButton(self.mifareOptionsPage)
        self.simulateMifareTagButton.setMinimumSize(QtCore.QSize(0, 80))
        self.simulateMifareTagButton.setObjectName("simulateMifareTagButton")
        self.verticalLayout_9.addWidget(self.simulateMifareTagButton)
        self.verticalLayout_12.addLayout(self.verticalLayout_9)
        self.mifareStackedWidget.addWidget(self.mifareOptionsPage)
        self.mifareResultsPage = QtWidgets.QWidget()
        self.mifareResultsPage.setObjectName("mifareResultsPage")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.mifareResultsPage)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.mifareTagInformationLabel = QtWidgets.QLabel(self.mifareResultsPage)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.mifareTagInformationLabel.setFont(font)
        self.mifareTagInformationLabel.setStyleSheet("color: rgb(33, 136, 145);")
        self.mifareTagInformationLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mifareTagInformationLabel.setObjectName("mifareTagInformationLabel")
        self.verticalLayout_13.addWidget(self.mifareTagInformationLabel)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.mifareTagResultsLabel = QtWidgets.QLabel(self.mifareResultsPage)
        self.mifareTagResultsLabel.setMinimumSize(QtCore.QSize(0, 230))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.mifareTagResultsLabel.setFont(font)
        self.mifareTagResultsLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 25, 51);\n"
"border-radius: 10;\n"
"padding: 10px;\n"
"border: 10px;")
        self.mifareTagResultsLabel.setText("")
        self.mifareTagResultsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mifareTagResultsLabel.setObjectName("mifareTagResultsLabel")
        self.verticalLayout_14.addWidget(self.mifareTagResultsLabel)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cloneMifareButton = QtWidgets.QPushButton(self.mifareResultsPage)
        self.cloneMifareButton.setMinimumSize(QtCore.QSize(120, 80))
        self.cloneMifareButton.setObjectName("cloneMifareButton")
        self.gridLayout_2.addWidget(self.cloneMifareButton, 0, 0, 1, 1)
        self.simulateMifareButton = QtWidgets.QPushButton(self.mifareResultsPage)
        self.simulateMifareButton.setMinimumSize(QtCore.QSize(120, 80))
        self.simulateMifareButton.setObjectName("simulateMifareButton")
        self.gridLayout_2.addWidget(self.simulateMifareButton, 0, 1, 1, 1)
        self.viewMemoryMifareButton = QtWidgets.QPushButton(self.mifareResultsPage)
        self.viewMemoryMifareButton.setMinimumSize(QtCore.QSize(120, 80))
        self.viewMemoryMifareButton.setObjectName("viewMemoryMifareButton")
        self.gridLayout_2.addWidget(self.viewMemoryMifareButton, 1, 0, 1, 1)
        self.backMifareButton = QtWidgets.QPushButton(self.mifareResultsPage)
        self.backMifareButton.setMinimumSize(QtCore.QSize(120, 80))
        self.backMifareButton.setStyleSheet("background-color: rgb(204, 0, 4);")
        self.backMifareButton.setObjectName("backMifareButton")
        self.gridLayout_2.addWidget(self.backMifareButton, 1, 1, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout_2)
        self.mifareStackedWidget.addWidget(self.mifareResultsPage)
        self.verticalLayout_11.addWidget(self.mifareStackedWidget)
        self.stackedWidget.addWidget(self.mifarePage)
        self.otherPage = QtWidgets.QWidget()
        self.otherPage.setObjectName("otherPage")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.otherPage)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.stackedWidget.addWidget(self.otherPage)
        self.mainMenuPage = QtWidgets.QWidget()
        self.mainMenuPage.setObjectName("mainMenuPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainMenuPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.customCommandButton = QtWidgets.QPushButton(self.mainMenuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customCommandButton.sizePolicy().hasHeightForWidth())
        self.customCommandButton.setSizePolicy(sizePolicy)
        self.customCommandButton.setObjectName("customCommandButton")
        self.gridLayout.addWidget(self.customCommandButton, 1, 3, 1, 1)
        self.savedTagsButton = QtWidgets.QPushButton(self.mainMenuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savedTagsButton.sizePolicy().hasHeightForWidth())
        self.savedTagsButton.setSizePolicy(sizePolicy)
        self.savedTagsButton.setObjectName("savedTagsButton")
        self.gridLayout.addWidget(self.savedTagsButton, 1, 1, 1, 1)
        self.tagInfoButton = QtWidgets.QPushButton(self.mainMenuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagInfoButton.sizePolicy().hasHeightForWidth())
        self.tagInfoButton.setSizePolicy(sizePolicy)
        self.tagInfoButton.setObjectName("tagInfoButton")
        self.gridLayout.addWidget(self.tagInfoButton, 0, 1, 1, 1)
        self.mifareButton = QtWidgets.QPushButton(self.mainMenuPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mifareButton.sizePolicy().hasHeightForWidth())
        self.mifareButton.setSizePolicy(sizePolicy)
        self.mifareButton.setObjectName("mifareButton")
        self.gridLayout.addWidget(self.mifareButton, 0, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.stackedWidget.addWidget(self.mainMenuPage)
        self.connectingMessagePage = QtWidgets.QWidget()
        self.connectingMessagePage.setObjectName("connectingMessagePage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.connectingMessagePage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.connectingProxmarkLabel = QtWidgets.QLabel(self.connectingMessagePage)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.connectingProxmarkLabel.setFont(font)
        self.connectingProxmarkLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.connectingProxmarkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectingProxmarkLabel.setObjectName("connectingProxmarkLabel")
        self.verticalLayout_6.addWidget(self.connectingProxmarkLabel)
        self.connectionStatusLabel = QtWidgets.QLabel(self.connectingMessagePage)
        self.connectionStatusLabel.setText("")
        self.connectionStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectionStatusLabel.setObjectName("connectionStatusLabel")
        self.verticalLayout_6.addWidget(self.connectionStatusLabel)
        self.connectionOkButton = QtWidgets.QPushButton(self.connectingMessagePage)
        self.connectionOkButton.setEnabled(True)
        self.connectionOkButton.setMinimumSize(QtCore.QSize(0, 80))
        self.connectionOkButton.setObjectName("connectionOkButton")
        self.verticalLayout_6.addWidget(self.connectionOkButton)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.connectingMessagePage)
        self.tagDetailsPage = QtWidgets.QWidget()
        self.tagDetailsPage.setStyleSheet("")
        self.tagDetailsPage.setObjectName("tagDetailsPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tagDetailsPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tagInformationTitleLabel = QtWidgets.QLabel(self.tagDetailsPage)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.tagInformationTitleLabel.setFont(font)
        self.tagInformationTitleLabel.setStyleSheet("color: rgb(33, 136, 145);")
        self.tagInformationTitleLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tagInformationTitleLabel.setObjectName("tagInformationTitleLabel")
        self.verticalLayout_4.addWidget(self.tagInformationTitleLabel)
        self.tagInformationLabel = QtWidgets.QLabel(self.tagDetailsPage)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tagInformationLabel.setFont(font)
        self.tagInformationLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.tagInformationLabel.setText("")
        self.tagInformationLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tagInformationLabel.setObjectName("tagInformationLabel")
        self.verticalLayout_4.addWidget(self.tagInformationLabel)
        self.tagInformationOkButton = QtWidgets.QPushButton(self.tagDetailsPage)
        self.tagInformationOkButton.setMinimumSize(QtCore.QSize(0, 80))
        self.tagInformationOkButton.setObjectName("tagInformationOkButton")
        self.verticalLayout_4.addWidget(self.tagInformationOkButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.tagDetailsPage)
        self.verticalLayout_8.addWidget(self.stackedWidget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pxmkappLabel.setText(_translate("MainWindow", "PXMKAPP"))
        self.connectProxmarkButton.setText(_translate("MainWindow", "CONNECT PROXMARK"))
        self.readMifareTagButton.setText(_translate("MainWindow", "READ TAG"))
        self.cloneMifareTagButton.setText(_translate("MainWindow", "CLONE TAG"))
        self.simulateMifareTagButton.setText(_translate("MainWindow", "SIMULATE TAG"))
        self.mifareTagInformationLabel.setText(_translate("MainWindow", "MIFARE TAG INFORMATION"))
        self.cloneMifareButton.setText(_translate("MainWindow", "CLONE"))
        self.simulateMifareButton.setText(_translate("MainWindow", "SIMULATE"))
        self.viewMemoryMifareButton.setText(_translate("MainWindow", "VIEW\n"
"MEMORY"))
        self.backMifareButton.setText(_translate("MainWindow", "BACK"))
        self.customCommandButton.setText(_translate("MainWindow", "CUSTOM\n"
"COMMAND"))
        self.savedTagsButton.setText(_translate("MainWindow", "SAVED\n"
"TAGS"))
        self.tagInfoButton.setText(_translate("MainWindow", "TAG\n"
"INFO"))
        self.mifareButton.setText(_translate("MainWindow", "MIFARE"))
        self.connectingProxmarkLabel.setText(_translate("MainWindow", "Connecting to the Proxmark..."))
        self.connectionOkButton.setText(_translate("MainWindow", "OK"))
        self.tagInformationTitleLabel.setText(_translate("MainWindow", "TAG INFORMATION"))
        self.tagInformationOkButton.setText(_translate("MainWindow", "OK"))
