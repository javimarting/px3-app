import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from MainWindow3 import Ui_MainWindow
import proxmark

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

        self.connectProxmarkButton.pressed.connect(self.start_connection)
        self.connectionOkButton.pressed.connect(self.return_to_connection_page)

    def start_connection(self):
        self.stackedWidget.setCurrentWidget(self.connectingMessagePage)
        self.connection = proxmark.connect_proxmark()
        if self.connection:
            
            self.stackedWidget.setCurrentWidget(self.mainMenuPage)
        else:
            self.connectionOkButton.show()
            self.connectionStatusLabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.connectionStatusLabel.setText("Could not establish connection")

    
    def return_to_connection_page(self):
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)
        self.connectionOkButton.hide()
        



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
