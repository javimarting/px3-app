# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
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
        MainWindow.setMinimumSize(QtCore.QSize(480, 700))
        MainWindow.setMaximumSize(QtCore.QSize(480, 750))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: #111927;\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.topLogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.topLogoLabel.setStyleSheet("\n"
"padding: 10;\n"
"")
        self.topLogoLabel.setText("")
        self.topLogoLabel.setPixmap(QtGui.QPixmap(":/icons/app-logo-icon-small.png"))
        self.topLogoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLogoLabel.setObjectName("topLogoLabel")
        self.verticalLayout_8.addWidget(self.topLogoLabel)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("QWidget {\n"
"border-radius: 15;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"color: #93dd03;\n"
"background-color: #111927;\n"
"border-radius: 15;\n"
"border: 1px solid;\n"
"border-color: #93dd03;\n"
"font-size: 15pt;\n"
"margin: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #93dd03;\n"
"color: #111927;\n"
"}\n"
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
        self.connectionPageContainer = QtWidgets.QWidget(self.connectProxmarkPage)
        self.connectionPageContainer.setObjectName("connectionPageContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.connectionPageContainer)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pxmkappLabel = QtWidgets.QLabel(self.connectionPageContainer)
        self.pxmkappLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.pxmkappLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pxmkappLabel.setFont(font)
        self.pxmkappLabel.setStyleSheet("")
        self.pxmkappLabel.setText("")
        self.pxmkappLabel.setPixmap(QtGui.QPixmap(":/icons/app-logo-icon.png"))
        self.pxmkappLabel.setScaledContents(False)
        self.pxmkappLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pxmkappLabel.setObjectName("pxmkappLabel")
        self.verticalLayout_9.addWidget(self.pxmkappLabel)
        self.connectProxmarkButton = QtWidgets.QPushButton(self.connectionPageContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectProxmarkButton.sizePolicy().hasHeightForWidth())
        self.connectProxmarkButton.setSizePolicy(sizePolicy)
        self.connectProxmarkButton.setMinimumSize(QtCore.QSize(350, 150))
        self.connectProxmarkButton.setMaximumSize(QtCore.QSize(600, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.connectProxmarkButton.setFont(font)
        self.connectProxmarkButton.setAutoFillBackground(False)
        self.connectProxmarkButton.setStyleSheet("")
        self.connectProxmarkButton.setObjectName("connectProxmarkButton")
        self.verticalLayout_9.addWidget(self.connectProxmarkButton)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem)
        self.verticalLayout.addWidget(self.connectionPageContainer, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.connectProxmarkPage)
        self.mifarePage = QtWidgets.QWidget()
        self.mifarePage.setObjectName("mifarePage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.mifarePage)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.mifareStackedWidget = QtWidgets.QStackedWidget(self.mifarePage)
        self.mifareStackedWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.mifareStackedWidget.setStyleSheet("QStackedWidget {\n"
"border-radius: 10;\n"
"background-color: #1a2332;\n"
"}")
        self.mifareStackedWidget.setObjectName("mifareStackedWidget")
        self.mifareOptionsPage = QtWidgets.QWidget()
        self.mifareOptionsPage.setObjectName("mifareOptionsPage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.mifareOptionsPage)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.mifareOptionsContainer = QtWidgets.QWidget(self.mifareOptionsPage)
        self.mifareOptionsContainer.setMinimumSize(QtCore.QSize(400, 0))
        self.mifareOptionsContainer.setAutoFillBackground(False)
        self.mifareOptionsContainer.setStyleSheet("QWidget#mifareOptionsContainer {\n"
"background-color: #1a2332;\n"
"}")
        self.mifareOptionsContainer.setObjectName("mifareOptionsContainer")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.mifareOptionsContainer)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label = QtWidgets.QLabel(self.mifareOptionsContainer)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_20.addWidget(self.label)
        self.mfAutopwnButton = QtWidgets.QPushButton(self.mifareOptionsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mfAutopwnButton.sizePolicy().hasHeightForWidth())
        self.mfAutopwnButton.setSizePolicy(sizePolicy)
        self.mfAutopwnButton.setMinimumSize(QtCore.QSize(0, 150))
        self.mfAutopwnButton.setAutoFillBackground(False)
        self.mfAutopwnButton.setObjectName("mfAutopwnButton")
        self.verticalLayout_20.addWidget(self.mfAutopwnButton)
        self.savedTagsButton = QtWidgets.QPushButton(self.mifareOptionsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savedTagsButton.sizePolicy().hasHeightForWidth())
        self.savedTagsButton.setSizePolicy(sizePolicy)
        self.savedTagsButton.setMinimumSize(QtCore.QSize(0, 150))
        self.savedTagsButton.setObjectName("savedTagsButton")
        self.verticalLayout_20.addWidget(self.savedTagsButton)
        self.verticalLayout_12.addWidget(self.mifareOptionsContainer)
        self.mifareStackedWidget.addWidget(self.mifareOptionsPage)
        self.mifareSavedTagsPage = QtWidgets.QWidget()
        self.mifareSavedTagsPage.setObjectName("mifareSavedTagsPage")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.mifareSavedTagsPage)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.mifareSavedTagsContainer = QtWidgets.QWidget(self.mifareSavedTagsPage)
        self.mifareSavedTagsContainer.setMinimumSize(QtCore.QSize(380, 0))
        self.mifareSavedTagsContainer.setStyleSheet("QWidget#mifareSavedTagsContainer {\n"
"background-color: #1a2332;\n"
"border-radius: 10;\n"
"}")
        self.mifareSavedTagsContainer.setObjectName("mifareSavedTagsContainer")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.mifareSavedTagsContainer)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.mifareSavedTagsPageLabel = QtWidgets.QLabel(self.mifareSavedTagsContainer)
        self.mifareSavedTagsPageLabel.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.mifareSavedTagsPageLabel.setFont(font)
        self.mifareSavedTagsPageLabel.setStyleSheet("color: #93dd03;\n"
"background-color: #111927;\n"
"border-radius: 15;\n"
"margin: 5px;\n"
"margin-left: 40px;\n"
"margin-right: 40px;")
        self.mifareSavedTagsPageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mifareSavedTagsPageLabel.setObjectName("mifareSavedTagsPageLabel")
        self.verticalLayout_16.addWidget(self.mifareSavedTagsPageLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mfTagsListView = QtWidgets.QListView(self.mifareSavedTagsContainer)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mfTagsListView.setFont(font)
        self.mfTagsListView.setStyleSheet("\n"
"QListView:item {\n"
"padding: 10;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"margin: 30px 0 30px 0;\n"
"width: 35px;\n"
"border-right: 1px solid #93dd03;\n"
"border-left: 1px solid #93dd03;\n"
"background-color: #263143;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical {\n"
"border: 1px solid #93dd03;\n"
"background-color: #111927;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"border: 1px solid #93dd03;\n"
"height: 30px;\n"
"border-top-left-radius: 7px;\n"
"border-top-right-radius: 7px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"background-color: #111927;\n"
"color: #93dd03;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"border: 1px solid #93dd03;\n"
"height: 30px;\n"
"border-bottom-left-radius: 7px;\n"
"border-bottom-right-radius: 7px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"background-color: #111927;\n"
"color: #93dd03;\n"
"}")
        self.mfTagsListView.setAlternatingRowColors(True)
        self.mfTagsListView.setObjectName("mfTagsListView")
        self.horizontalLayout_2.addWidget(self.mfTagsListView)
        self.verticalLayout_16.addLayout(self.horizontalLayout_2)
        self.mifareSavedTagsButtonContainer = QtWidgets.QWidget(self.mifareSavedTagsContainer)
        self.mifareSavedTagsButtonContainer.setMinimumSize(QtCore.QSize(300, 30))
        self.mifareSavedTagsButtonContainer.setStyleSheet("QPushButton {\n"
"padding: 3;\n"
"margin: 2px;\n"
"}")
        self.mifareSavedTagsButtonContainer.setObjectName("mifareSavedTagsButtonContainer")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.mifareSavedTagsButtonContainer)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mfInfoButton = QtWidgets.QPushButton(self.mifareSavedTagsButtonContainer)
        self.mfInfoButton.setMinimumSize(QtCore.QSize(100, 50))
        self.mfInfoButton.setObjectName("mfInfoButton")
        self.horizontalLayout_4.addWidget(self.mfInfoButton)
        self.mfCloneButton = QtWidgets.QPushButton(self.mifareSavedTagsButtonContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mfCloneButton.sizePolicy().hasHeightForWidth())
        self.mfCloneButton.setSizePolicy(sizePolicy)
        self.mfCloneButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mfCloneButton.setFont(font)
        self.mfCloneButton.setObjectName("mfCloneButton")
        self.horizontalLayout_4.addWidget(self.mfCloneButton)
        self.mfSimulateButton = QtWidgets.QPushButton(self.mifareSavedTagsButtonContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mfSimulateButton.sizePolicy().hasHeightForWidth())
        self.mfSimulateButton.setSizePolicy(sizePolicy)
        self.mfSimulateButton.setMinimumSize(QtCore.QSize(100, 50))
        self.mfSimulateButton.setObjectName("mfSimulateButton")
        self.horizontalLayout_4.addWidget(self.mfSimulateButton)
        self.verticalLayout_22.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mfGiveNameButton = QtWidgets.QPushButton(self.mifareSavedTagsButtonContainer)
        self.mfGiveNameButton.setMinimumSize(QtCore.QSize(100, 50))
        self.mfGiveNameButton.setObjectName("mfGiveNameButton")
        self.horizontalLayout_5.addWidget(self.mfGiveNameButton)
        self.mfDeleteButton = QtWidgets.QPushButton(self.mifareSavedTagsButtonContainer)
        self.mfDeleteButton.setMinimumSize(QtCore.QSize(100, 50))
        self.mfDeleteButton.setStyleSheet("QPushButton {\n"
"color: #c43437;\n"
"border: 1px solid;\n"
"border-color: #c43437;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #c43437;\n"
"color: #111927;\n"
"}")
        self.mfDeleteButton.setIconSize(QtCore.QSize(32, 32))
        self.mfDeleteButton.setObjectName("mfDeleteButton")
        self.horizontalLayout_5.addWidget(self.mfDeleteButton)
        self.verticalLayout_22.addLayout(self.horizontalLayout_5)
        self.verticalLayout_16.addWidget(self.mifareSavedTagsButtonContainer)
        self.verticalLayout_17.addWidget(self.mifareSavedTagsContainer)
        self.mifareStackedWidget.addWidget(self.mifareSavedTagsPage)
        self.mifareSimulatePage = QtWidgets.QWidget()
        self.mifareSimulatePage.setMinimumSize(QtCore.QSize(380, 0))
        self.mifareSimulatePage.setObjectName("mifareSimulatePage")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.mifareSimulatePage)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.mifareSimulateContainer = QtWidgets.QWidget(self.mifareSimulatePage)
        self.mifareSimulateContainer.setStyleSheet("QWidget#mifareSimulateContainer {\n"
"background-color: #1a2332;\n"
"border-radius: 10;\n"
"}")
        self.mifareSimulateContainer.setObjectName("mifareSimulateContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.mifareSimulateContainer)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.mifareSimulateTitleLabel = QtWidgets.QLabel(self.mifareSimulateContainer)
        self.mifareSimulateTitleLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.mifareSimulateTitleLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mifareSimulateTitleLabel.setFont(font)
        self.mifareSimulateTitleLabel.setStyleSheet("color: #93dd03;\n"
"background-color: #111927;\n"
"border-radius: 15;\n"
"margin: 5px;\n"
"margin-left: 40px;\n"
"margin-right: 40px;")
        self.mifareSimulateTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mifareSimulateTitleLabel.setObjectName("mifareSimulateTitleLabel")
        self.verticalLayout_15.addWidget(self.mifareSimulateTitleLabel)
        self.mifareSimulateLabel = QtWidgets.QLabel(self.mifareSimulateContainer)
        self.mifareSimulateLabel.setStyleSheet("padding: 5;")
        self.mifareSimulateLabel.setText("")
        self.mifareSimulateLabel.setWordWrap(True)
        self.mifareSimulateLabel.setObjectName("mifareSimulateLabel")
        self.verticalLayout_15.addWidget(self.mifareSimulateLabel)
        self.startSimulatingButton = QtWidgets.QPushButton(self.mifareSimulateContainer)
        self.startSimulatingButton.setMinimumSize(QtCore.QSize(0, 100))
        self.startSimulatingButton.setObjectName("startSimulatingButton")
        self.verticalLayout_15.addWidget(self.startSimulatingButton)
        self.verticalLayout_14.addWidget(self.mifareSimulateContainer)
        self.mifareStackedWidget.addWidget(self.mifareSimulatePage)
        self.verticalLayout_11.addWidget(self.mifareStackedWidget, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.mifarePage)
        self.resultsPage = QtWidgets.QWidget()
        self.resultsPage.setObjectName("resultsPage")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.resultsPage)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.resultsPageContainer = QtWidgets.QWidget(self.resultsPage)
        self.resultsPageContainer.setStyleSheet("QWidget#resultsPageContainer {\n"
"background-color: #1a2332;\n"
"border-radius: 10;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"margin: 30px 0 30px 0;\n"
"width: 35px;\n"
"border-right: 1px solid #93dd03;\n"
"border-left: 1px solid #93dd03;\n"
"background-color: #263143;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical {\n"
"border: 1px solid #93dd03;\n"
"background-color: #111927;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"border: 1px solid #93dd03;\n"
"height: 30px;\n"
"border-top-left-radius: 7px;\n"
"border-top-right-radius: 7px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"background-color: #111927;\n"
"color: #93dd03;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"border: 1px solid #93dd03;\n"
"height: 30px;\n"
"border-bottom-left-radius: 7px;\n"
"border-bottom-right-radius: 7px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"background-color: #111927;\n"
"color: #93dd03;\n"
"}\n"
"")
        self.resultsPageContainer.setObjectName("resultsPageContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.resultsPageContainer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultsPageTitleLabel = QtWidgets.QLabel(self.resultsPageContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsPageTitleLabel.sizePolicy().hasHeightForWidth())
        self.resultsPageTitleLabel.setSizePolicy(sizePolicy)
        self.resultsPageTitleLabel.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.resultsPageTitleLabel.setFont(font)
        self.resultsPageTitleLabel.setStyleSheet("color: #93dd03;\n"
"background-color: #111927;\n"
"border-radius: 15;\n"
"margin: 5px;\n"
"margin-left: 40px;\n"
"margin-right: 40px;")
        self.resultsPageTitleLabel.setText("")
        self.resultsPageTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsPageTitleLabel.setObjectName("resultsPageTitleLabel")
        self.verticalLayout_2.addWidget(self.resultsPageTitleLabel)
        self.resultsPageScrollArea = QtWidgets.QScrollArea(self.resultsPageContainer)
        self.resultsPageScrollArea.setMinimumSize(QtCore.QSize(400, 0))
        self.resultsPageScrollArea.setStyleSheet("")
        self.resultsPageScrollArea.setWidgetResizable(True)
        self.resultsPageScrollArea.setObjectName("resultsPageScrollArea")
        self.resultsPageScrollAreaWidgetContents = QtWidgets.QWidget()
        self.resultsPageScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 311))
        self.resultsPageScrollAreaWidgetContents.setObjectName("resultsPageScrollAreaWidgetContents")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.resultsPageScrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.resultsPageDataLabel = QtWidgets.QLabel(self.resultsPageScrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsPageDataLabel.sizePolicy().hasHeightForWidth())
        self.resultsPageDataLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.resultsPageDataLabel.setFont(font)
        self.resultsPageDataLabel.setStyleSheet("")
        self.resultsPageDataLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultsPageDataLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.resultsPageDataLabel.setText("")
        self.resultsPageDataLabel.setScaledContents(False)
        self.resultsPageDataLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultsPageDataLabel.setWordWrap(True)
        self.resultsPageDataLabel.setObjectName("resultsPageDataLabel")
        self.verticalLayout_21.addWidget(self.resultsPageDataLabel)
        self.resultsPageScrollArea.setWidget(self.resultsPageScrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.resultsPageScrollArea)
        self.resultsPageButtonContainer = QtWidgets.QWidget(self.resultsPageContainer)
        self.resultsPageButtonContainer.setStyleSheet("QPushButton {\n"
"font-size: 15pt;\n"
"margin: 1;\n"
"}")
        self.resultsPageButtonContainer.setObjectName("resultsPageButtonContainer")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.resultsPageButtonContainer)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.resultsPageButton1 = QtWidgets.QPushButton(self.resultsPageButtonContainer)
        self.resultsPageButton1.setMinimumSize(QtCore.QSize(0, 50))
        self.resultsPageButton1.setText("")
        self.resultsPageButton1.setObjectName("resultsPageButton1")
        self.horizontalLayout_8.addWidget(self.resultsPageButton1)
        self.resultsPageButton2 = QtWidgets.QPushButton(self.resultsPageButtonContainer)
        self.resultsPageButton2.setMinimumSize(QtCore.QSize(0, 50))
        self.resultsPageButton2.setText("")
        self.resultsPageButton2.setObjectName("resultsPageButton2")
        self.horizontalLayout_8.addWidget(self.resultsPageButton2)
        self.verticalLayout_2.addWidget(self.resultsPageButtonContainer)
        self.verticalLayout_10.addWidget(self.resultsPageContainer, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.resultsPage)
        self.mainMenuPage = QtWidgets.QWidget()
        self.mainMenuPage.setStyleSheet("QWidget#mainMenuPage {\n"
"margin: 0;\n"
"padding: 0px;\n"
"}")
        self.mainMenuPage.setObjectName("mainMenuPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainMenuPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mainMenuContainer = QtWidgets.QWidget(self.mainMenuPage)
        self.mainMenuContainer.setMinimumSize(QtCore.QSize(380, 0))
        self.mainMenuContainer.setStyleSheet("QWidget#mainMenuContainer {\n"
"padding: 20px;\n"
"background-color: #1a2332;\n"
"border-radius: 15;\n"
"}")
        self.mainMenuContainer.setObjectName("mainMenuContainer")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.mainMenuContainer)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.mainMenuLabel = QtWidgets.QLabel(self.mainMenuContainer)
        self.mainMenuLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.mainMenuLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mainMenuLabel.setFont(font)
        self.mainMenuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainMenuLabel.setObjectName("mainMenuLabel")
        self.verticalLayout_23.addWidget(self.mainMenuLabel)
        self.basicCommandsButton = QtWidgets.QPushButton(self.mainMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basicCommandsButton.sizePolicy().hasHeightForWidth())
        self.basicCommandsButton.setSizePolicy(sizePolicy)
        self.basicCommandsButton.setMinimumSize(QtCore.QSize(200, 120))
        self.basicCommandsButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.basicCommandsButton.setFont(font)
        self.basicCommandsButton.setStyleSheet("")
        self.basicCommandsButton.setObjectName("basicCommandsButton")
        self.verticalLayout_23.addWidget(self.basicCommandsButton)
        self.mifare1kButton = QtWidgets.QPushButton(self.mainMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mifare1kButton.sizePolicy().hasHeightForWidth())
        self.mifare1kButton.setSizePolicy(sizePolicy)
        self.mifare1kButton.setMinimumSize(QtCore.QSize(200, 120))
        self.mifare1kButton.setMaximumSize(QtCore.QSize(1777777, 1777777))
        self.mifare1kButton.setObjectName("mifare1kButton")
        self.verticalLayout_23.addWidget(self.mifare1kButton)
        self.customCommandButton = QtWidgets.QPushButton(self.mainMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customCommandButton.sizePolicy().hasHeightForWidth())
        self.customCommandButton.setSizePolicy(sizePolicy)
        self.customCommandButton.setMinimumSize(QtCore.QSize(200, 120))
        self.customCommandButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.customCommandButton.setObjectName("customCommandButton")
        self.verticalLayout_23.addWidget(self.customCommandButton)
        self.verticalLayout_5.addWidget(self.mainMenuContainer)
        self.stackedWidget.addWidget(self.mainMenuPage)
        self.basicCommandsPage = QtWidgets.QWidget()
        self.basicCommandsPage.setStyleSheet("")
        self.basicCommandsPage.setObjectName("basicCommandsPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.basicCommandsPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.basicCommandsContainer = QtWidgets.QWidget(self.basicCommandsPage)
        self.basicCommandsContainer.setStyleSheet("QWidget#basicCommandsContainer {\n"
"padding: 20px;\n"
"background-color: #1a2332;\n"
"border-radius: 15;\n"
"}")
        self.basicCommandsContainer.setObjectName("basicCommandsContainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.basicCommandsContainer)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.basicCommandsLabel = QtWidgets.QLabel(self.basicCommandsContainer)
        self.basicCommandsLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.basicCommandsLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.basicCommandsLabel.setFont(font)
        self.basicCommandsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.basicCommandsLabel.setObjectName("basicCommandsLabel")
        self.verticalLayout_4.addWidget(self.basicCommandsLabel)
        self.hwStatusButton = QtWidgets.QPushButton(self.basicCommandsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hwStatusButton.sizePolicy().hasHeightForWidth())
        self.hwStatusButton.setSizePolicy(sizePolicy)
        self.hwStatusButton.setMinimumSize(QtCore.QSize(0, 120))
        self.hwStatusButton.setObjectName("hwStatusButton")
        self.verticalLayout_4.addWidget(self.hwStatusButton)
        self.autoDetectTagButton = QtWidgets.QPushButton(self.basicCommandsContainer)
        self.autoDetectTagButton.setMinimumSize(QtCore.QSize(0, 120))
        self.autoDetectTagButton.setObjectName("autoDetectTagButton")
        self.verticalLayout_4.addWidget(self.autoDetectTagButton)
        self.readLFTagButton = QtWidgets.QPushButton(self.basicCommandsContainer)
        self.readLFTagButton.setMinimumSize(QtCore.QSize(0, 120))
        self.readLFTagButton.setObjectName("readLFTagButton")
        self.verticalLayout_4.addWidget(self.readLFTagButton)
        self.readHFTagButton = QtWidgets.QPushButton(self.basicCommandsContainer)
        self.readHFTagButton.setMinimumSize(QtCore.QSize(0, 120))
        self.readHFTagButton.setObjectName("readHFTagButton")
        self.verticalLayout_4.addWidget(self.readHFTagButton)
        self.verticalLayout_3.addWidget(self.basicCommandsContainer)
        self.stackedWidget.addWidget(self.basicCommandsPage)
        self.enterTextPage = QtWidgets.QWidget()
        self.enterTextPage.setObjectName("enterTextPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.enterTextPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.enterTextContainer = QtWidgets.QWidget(self.enterTextPage)
        self.enterTextContainer.setStyleSheet("QWidget#customCommandContainer {\n"
"padding: 20px;\n"
"background-color: #1a2332;\n"
"border-radius: 15;\n"
"}")
        self.enterTextContainer.setObjectName("enterTextContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.enterTextContainer)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textEdit = QtWidgets.QLineEdit(self.enterTextContainer)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"padding: 10;\n"
"margin: 5px;")
        self.textEdit.setPlaceholderText("")
        self.textEdit.setClearButtonEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.enterTextButton = QtWidgets.QPushButton(self.enterTextContainer)
        self.enterTextButton.setMinimumSize(QtCore.QSize(0, 80))
        self.enterTextButton.setStyleSheet("margin: 5px;")
        self.enterTextButton.setText("")
        self.enterTextButton.setObjectName("enterTextButton")
        self.verticalLayout_6.addWidget(self.enterTextButton)
        self.verticalLayout_7.addWidget(self.enterTextContainer)
        self.stackedWidget.addWidget(self.enterTextPage)
        self.changeTagNamePage = QtWidgets.QWidget()
        self.changeTagNamePage.setStyleSheet("")
        self.changeTagNamePage.setObjectName("changeTagNamePage")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.changeTagNamePage)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.lineEdit = QtWidgets.QLineEdit(self.changeTagNamePage)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_24.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.changeTagNamePage)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_24.addWidget(self.pushButton)
        self.verticalLayout_19.addLayout(self.verticalLayout_24)
        self.stackedWidget.addWidget(self.changeTagNamePage)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        self.verticalLayout_13.addLayout(self.verticalLayout_8)
        self.backExitContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backExitContainer.sizePolicy().hasHeightForWidth())
        self.backExitContainer.setSizePolicy(sizePolicy)
        self.backExitContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.backExitContainer.setStyleSheet(".QWidget {\n"
"/*background-color: #1a2332;*/\n"
"border-radius: 15;\n"
"}\n"
"QPushButton {\n"
"border-radius: 15;\n"
"background-color: #111927;\n"
"margin: 10px;\n"
"}")
        self.backExitContainer.setObjectName("backExitContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.backExitContainer)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.backButton = QtWidgets.QPushButton(self.backExitContainer)
        self.backButton.setMinimumSize(QtCore.QSize(120, 80))
        self.backButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
"color: #93dd03;\n"
"border: 1px solid;\n"
"border-color: #93dd03;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #93dd03;\n"
"color: #111927;\n"
"}\n"
"")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_3.addWidget(self.backButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.exitButton = QtWidgets.QPushButton(self.backExitContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QtCore.QSize(120, 80))
        self.exitButton.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton {\n"
"color: #c43437;\n"
"border: 1px solid;\n"
"border-color: #c43437;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #c43437;\n"
"color: #111927;\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.verticalLayout_13.addWidget(self.backExitContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.mifareStackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PX3-APP"))
        self.connectProxmarkButton.setText(_translate("MainWindow", "CONNECT PROXMARK"))
        self.label.setText(_translate("MainWindow", "MIFARE CLASSIC"))
        self.mfAutopwnButton.setText(_translate("MainWindow", "AUTOPWN TAG"))
        self.savedTagsButton.setText(_translate("MainWindow", "SAVED TAGS"))
        self.mifareSavedTagsPageLabel.setText(_translate("MainWindow", "SAVED TAGS"))
        self.mfInfoButton.setText(_translate("MainWindow", "INFO"))
        self.mfCloneButton.setText(_translate("MainWindow", "CLONE"))
        self.mfSimulateButton.setText(_translate("MainWindow", "SIMULATE"))
        self.mfGiveNameButton.setText(_translate("MainWindow", "GIVE NAME"))
        self.mfDeleteButton.setText(_translate("MainWindow", "DELETE"))
        self.mifareSimulateTitleLabel.setText(_translate("MainWindow", "SIMULATE MIFARE 1K TAG"))
        self.startSimulatingButton.setText(_translate("MainWindow", "START"))
        self.mainMenuLabel.setText(_translate("MainWindow", "MAIN MENU"))
        self.basicCommandsButton.setText(_translate("MainWindow", "BASIC COMMANDS"))
        self.mifare1kButton.setText(_translate("MainWindow", "MIFARE CLASSIC"))
        self.customCommandButton.setText(_translate("MainWindow", "CUSTOM\n"
"COMMAND"))
        self.basicCommandsLabel.setText(_translate("MainWindow", "BASIC COMMANDS"))
        self.hwStatusButton.setText(_translate("MainWindow", "HARDWARE STATUS"))
        self.autoDetectTagButton.setText(_translate("MainWindow", "AUTO-DETECT TAG"))
        self.readLFTagButton.setText(_translate("MainWindow", "READ LOW-FREQUENCY TAG"))
        self.readHFTagButton.setText(_translate("MainWindow", "READ HIGH-FREQUENCY TAG"))
        self.pushButton.setText(_translate("MainWindow", "DONE"))
        self.backButton.setText(_translate("MainWindow", "BACK"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
from px3_app.ui import resources_rc
