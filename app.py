import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from MainWindow3 import Ui_MainWindow
from proxmark import Proxmark, Worker, pchild
import pexpect
import utils


worker_thread = None
proxmark_worker = None
proxmark_child = None



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.worker_thread = QThread()
        self.proxmark_worker = Proxmark()
        self.proxmark_worker.moveToThread(self.worker_thread)

        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

        self.connectProxmarkButton.clicked.connect(self.show_connecting_page)
        self.connectProxmarkButton.clicked.connect(self.start_connection)
        self.connectionOkButton.clicked.connect(self.return_to_connection_page)
        self.tagInformationOkButton.clicked.connect(self.show_main_menu_page)
        self.tagInfoButton.clicked.connect(self.show_tag_info_page)
        self.tagInfoButton.clicked.connect(self.read_tag)
        self.mifareButton.clicked.connect(self.show_tag_info_page)
        self.mifareButton.clicked.connect(self.read_hf_tag)

    def show_connecting_page(self):
        self.connectionOkButton.hide()
        self.connectionStatusLabel.hide()
        self.stackedWidget.setCurrentWidget(self.connectingMessagePage)

    def show_main_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
    
    def read_hf_tag(self):
        global proxmark_worker
        result = self.proxmark_worker.read_mifare_hf_tag()
        if result:
            utils.analyze_result_files(result)
            text = "UID: 56 45 32 34\nDATE: 2/21/2022\nKEY"
            self.tagInformationLabel.setText(text)
    
    def show_tag_info_page(self):
        self.tagInformationLabel.setText("")
        self.stackedWidget.setCurrentWidget(self.tagDetailsPage)
        
    def show_tag_info(self, info):
        self.tagInformationLabel.setText(info)
        
    
    def read_tag(self):
        global proxmark_worker
        result = self.proxmark_worker.read_tag()
        self.tagInformationLabel.setText(result)
        # self.stackedWidget.setCurrentWidget(self.tagDetailsPage)
        # thread = QThread()
        # proxmark_worker = Worker()
        # proxmark_worker.moveToThread(thread)
        # self.worker_thread.started.connect(self.proxmark_worker.read_tag)

        # self.proxmark_worker.successful_operation.connect(self.show_tag_info)
        # proxmark_worker.finished.connect(thread.quit)

        


    def successful_read(self, message):
        print(message)
        


    def start_connection(self):
        global worker_thread
        global proxmark_worker

        # worker_thread = QThread()
        # proxmark_worker = Proxmark()
        # proxmark_worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.proxmark_worker.connect_proxmark)
        self.proxmark_worker.connected.connect(self.handle_connected)
        self.proxmark_worker.not_connected.connect(self.handle_not_connected)
        # proxmark_worker.finished.connect(worker_thread.quit)
        self.worker_thread.start()
        

    def handle_connected(self, pexpect_object):
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
        self.proxmark_child = pexpect_object
        pchild = pexpect_object

    def handle_not_connected(self, string):
        print(string)
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
