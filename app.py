import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from MainWindow3 import Ui_MainWindow
from proxmark import Proxmark, Worker, pchild
from models import TableModel
import utils
from tags import Mifare1k



proxmark_worker = None
proxmark_child = None


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.last_mifare_tag_read = None
        self.memory_data = ['hola']
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
        self.mifareButton.clicked.connect(self.show_mifare_options_page)
        self.readMifareTagButton.clicked.connect(self.show_mifare_results_page)
        self.readMifareTagButton.clicked.connect(self.read_hf_tag)
        self.backMifareButton.clicked.connect(self.show_mifare_options_page)
        self.viewMemoryMifareButton.clicked.connect(self.show_memory_page)
        self.memoryOkButton.clicked.connect(self.show_mifare_options_page)

    def show_memory_page(self):
        self.mifareStackedWidget.setCurrentWidget(self.memoryLayoutPage)
        model = TableModel(self.last_mifare_tag_read.memory)
        self.memoryTableView.setModel(model)
        self.memoryTableView.resizeColumnsToContents()

    def show_connecting_page(self):
        self.connectionOkButton.hide()
        self.connectionStatusLabel.hide()
        self.stackedWidget.setCurrentWidget(self.connectingMessagePage)

    def show_main_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
    
    def show_mifare_options_page(self):
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareOptionsPage)
    
    def show_mifare_results_page(self):
        self.mifareStackedWidget.setCurrentWidget(self.mifareResultsPage)
    
    def read_hf_tag(self):
        result = self.proxmark_worker.read_mifare_hf_tag()
        if result:
            files = utils.analyze_result_files(result)
            print(files['json_file'])
            mifare_tag = Mifare1k(files)
            self.mifareTagResultsLabel.setText(mifare_tag.basic_info())
            self.last_mifare_tag_read = mifare_tag
    
    def show_tag_info_page(self):
        self.tagInformationLabel.setText("")
        self.stackedWidget.setCurrentWidget(self.tagDetailsPage)
        
    def show_tag_info(self, info):
        self.tagInformationLabel.setText(info)

    def read_tag(self):
        result = self.proxmark_worker.read_tag()
        self.tagInformationLabel.setText(result)

    def set_label_text(self, text):
        self.tagInformationLabel.setText(text)

    def start_connection(self):
        self.worker_thread.started.connect(self.proxmark_worker.connect_proxmark)
        self.proxmark_worker.connected.connect(self.handle_connected)
        self.proxmark_worker.not_connected.connect(self.handle_not_connected)
        self.worker_thread.start()

    def handle_connected(self, pexpect_object):
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
        self.proxmark_child = pexpect_object

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
