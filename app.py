import sys
from PyQt5 import QtWidgets

from MainWindow3 import Ui_MainWindow
from proxmark import Proxmark
import utils
from tags import Mifare1k


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_page = self.connectProxmarkPage
        self.actual_page = self.connectProxmarkPage
        self.backButton.hide()

        self.proxmark = Proxmark()

        self.proxmark_child = None

        self.last_mifare_tag_read = None

        self.proxmark_worker = Proxmark()

        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

        self.connectProxmarkButton.clicked.connect(self.start_connection)
        self.connectionOkButton.clicked.connect(self.return_to_connection_page)
        self.tagInformationOkButton.clicked.connect(self.show_main_menu_page)
        self.tagInfoButton.clicked.connect(self.show_results_page)
        self.tagInfoButton.clicked.connect(self.read_tag)
        self.mifareButton.clicked.connect(self.show_mifare_options_page)
        self.readMifareTagButton.clicked.connect(self.show_mifare_results_page)
        self.readMifareTagButton.clicked.connect(self.read_hf_tag)
        self.viewMemoryMifareButton.clicked.connect(self.show_memory_page)
        self.memoryOkButton.clicked.connect(self.show_mifare_options_page)
        self.mifareCloneResultsOkButton.clicked.connect(self.show_mifare_options_page)
        self.cloneMifareButton.clicked.connect(self.clone_mifare_1k_tag)
        self.backButton.clicked.connect(self.show_last_page)
        self.exitButton.clicked.connect(self.exit_app)

    def show_connect_proxmark_page(self):
        self.backButton.hide()
        self.actual_page = self.connectProxmarkPage
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

    def show_results_page(self):
        self.backButton.show()
        self.actual_page = self.resultsPage
        self.stackedWidget.setCurrentWidget(self.resultsPage)

    def set_results_data(self, successful, title, data, last_page):
        color = "color: rgb(255, 255, 255);"
        if not successful:
            color = "color: rgb(255, 0, 0);"
        self.resultsPageDataLabel.setStyleSheet(color)
        self.resultsPageTitleLabel.setText(title)
        self.resultsPageDataLabel.setText(data)
        self.last_page = last_page

    def start_connection(self):
        connection = self.proxmark.connect_proxmark()
        if connection:
            self.show_main_menu_page()
        else:
            title = "CONNECTION STATUS"
            data = "Couldn't establish connection"
            last_page = self.connectProxmarkPage
            self.set_results_data(False, title, data, last_page)
            self.show_results_page()

    def show_last_page(self):
        if self.last_page is self.mainMenuPage or self.last_page is self.connectProxmarkPage:
            self.backButton.hide()

        if self.actual_page is self.connectingMessagePage:
            self.connectionStatusLabel.setText("")
            self.show_connect_proxmark_page()
        elif self.actual_page is self.tagDetailsPage:
            self.tagInformationLabel.setText("")
            self.show_main_menu_page()
        elif self.actual_page is self.memoryLayoutPage:
            self.memoryLayoutLabel.setText("")
            self.show_mifare_options_page()
        elif self.actual_page is self.mifareResultsPage:
            self.mifareTagResultsLabel.setText("")
            self.show_mifare_options_page()
        elif self.actual_page is self.mifareOptionsPage:
            self.show_main_menu_page()
        elif self.actual_page is self.resultsPage:
            self.resultsPageDataLabel.setText("")

        if self.last_page is self.connectProxmarkPage:
            self.show_connect_proxmark_page()
        elif self.last_page is self.mainMenuPage:
            self.show_main_menu_page()

        # self.stackedWidget.setCurrentWidget(self.last_page)
        self.actual_page = self.last_page

    def show_memory_page(self):
        self.actual_page = self.memoryLayoutPage
        self.last_page = self.mifareOptionsPage
        self.mifareStackedWidget.setCurrentWidget(self.memoryLayoutPage)
        print(self.last_mifare_tag_read.memory_string())
        self.memoryLayoutLabel.setText(self.last_mifare_tag_read.memory_string())
        self.last_page = self.mifareOptionsPage

    def show_main_menu_page(self):
        self.backButton.hide()
        self.last_page = self.mainMenuPage
        self.actual_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)

    def show_tag_info_page(self):
        self.backButton.show()
        self.actual_page = self.tagDetailsPage
        self.stackedWidget.setCurrentWidget(self.tagDetailsPage)
    
    def show_mifare_options_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.actual_page = self.mifareOptionsPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareOptionsPage)
    
    def show_mifare_results_page(self):
        self.actual_page = self.mifareResultsPage
        self.mifareStackedWidget.setCurrentWidget(self.mifareResultsPage)
        self.last_page = self.mifareOptionsPage
    
    def read_hf_tag(self):
        result = self.proxmark_worker.read_mifare_hf_tag()
        if result:
            files = utils.analyze_result_files(result)
            mifare_tag = Mifare1k(files)
            self.mifareTagResultsLabel.setStyleSheet("color: rgb(255, 255, 255);")
            self.mifareTagResultsLabel.setText(mifare_tag.basic_info())
            self.manage_mifare_tag_information_buttons(True)
            self.last_mifare_tag_read = mifare_tag
        else:
            self.mifareTagResultsLabel.setText("Couldn't read tag")
            self.mifareTagResultsLabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.manage_mifare_tag_information_buttons(False)

    def manage_mifare_tag_information_buttons(self, bool):
        self.cloneMifareTagButton.setEnabled(bool)
        self.simulateMifareButton.setEnabled(bool)
        self.viewMemoryMifareButton.setEnabled(bool)

    def clone_mifare_1k_tag(self):
        eml_file = self.last_mifare_tag_read.eml_file
        print(eml_file)
        result = self.proxmark_worker.clone_mifare_1k_tag(eml_file)
        self.mifareStackedWidget.setCurrentWidget(self.mifareCloneResultsPage)
        self.last_page = self.mifareOptionsPage

        if result:
            self.mifareCloneResultsLabel.setStyleSheet("color: rgb(255, 255, 255);")
            self.mifareCloneResultsLabel.setText("Tag cloned successfully!")
        else:
            self.mifareCloneResultsLabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.mifareCloneResultsLabel.setText("Unable to clone tag")

    def read_tag(self):
        result = self.proxmark.read_tag()
        title = "TAG INFORMATION"
        data = ""
        if result:
            data = result
            self.set_results_data(True, title, result, self.mainMenuPage)
        else:
            data = "Couldn't read tag"
            self.set_results_data(False, title, data, self.mainMenuPage)


    def handle_connected(self, pexpect_object):
        self.show_main_menu_page()
        self.proxmark_child = pexpect_object

    def handle_not_connected(self, string):
        self.stackedWidget.setCurrentWidget(self.connectingMessagePage)
        self.connectionStatusLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.connectionStatusLabel.setText(string)
        self.backButton.show()
        self.actual_page = self.connectingMessagePage

    def return_to_connection_page(self):
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)
        self.connectionStatusLabel.setText("")

    def exit_app(self):
        sys.exit()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
