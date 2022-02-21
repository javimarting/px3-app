import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from MainWindow3 import Ui_MainWindow
from proxmark import Proxmark
import pexpect
import utils


worker_thread = None
proxmark_worker = None
proxmark_child = None



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

        self.connectProxmarkButton.clicked.connect(self.show_connecting_page)
        self.connectProxmarkButton.clicked.connect(self.start_connection)
        self.connectionOkButton.clicked.connect(self.return_to_connection_page)
        self.tagInformationOkButton.clicked.connect(self.show_main_menu_page)
        self.pushButton_3.clicked.connect(self.read_tag)

    def show_connecting_page(self):
        self.connectionOkButton.hide()
        self.connectionStatusLabel.hide()
        self.stackedWidget.setCurrentWidget(self.connectingMessagePage)

    def show_main_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
    
    def read_hf_tag(self):
        global proxmark_worker
        result = proxmark_worker.read_mifare_hf_tag()
        if result:
            utils.analyze_result_files(result)
            self.stackedWidget.setCurrentWidget(self.tagDetailsPage)
            text = "UID: 56 45 32 34\nDATE: 2/21/2022\nKEY"
            self.tagInformationLabel.setText(text)
    
    def read_tag(self):
        global proxmark_worker
        result = proxmark_worker.read_tag()
        self.tagInformationLabel.setText(result)
        self.stackedWidget.setCurrentWidget(self.tagDetailsPage)


    def successful_read(self, message):
        print(message)
        


    def start_connection(self):
        global worker_thread
        global proxmark_worker

        worker_thread = QThread()
        proxmark_worker = Proxmark()
        proxmark_worker.moveToThread(worker_thread)
        worker_thread.started.connect(proxmark_worker.connect_proxmark)
        proxmark_worker.connected.connect(self.handle_connected)
        proxmark_worker.not_connected.connect(self.handle_not_connected)
        proxmark_worker.finished.connect(worker_thread.quit)
        worker_thread.start()
        

    def handle_connected(self, pexpect_object):
        global proxmark_child

        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
        proxmark_child = pexpect_object

    def handle_not_connected(self, string):
        global worker_thread

        print(string)
        worker_thread.quit()
        self.connectionOkButton.show()
        self.connectionStatusLabel.show()
        self.connectionStatusLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.connectionStatusLabel.setText("Could not establish connection")

    
    def return_to_connection_page(self):
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)
        self.connectionOkButton.hide()
        self.connectionStatusLabel.setText("")
        



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
