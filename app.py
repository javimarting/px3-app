import sys
import re

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ansi2html import Ansi2HTMLConverter
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
        self.topLogoLabel.hide()

        self.proxmark = Proxmark()

        self.proxmark_child = None

        self.last_mifare_tag_read = None

        self.proxmark_worker = Proxmark()

        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

        self.connectProxmarkButton.clicked.connect(self.start_connection)
        self.autoDetectTagButton.clicked.connect(self.show_results_page)
        self.autoDetectTagButton.clicked.connect(self.read_tag)
        self.mifare1kButton.clicked.connect(self.show_mifare_options_page)
        self.readMifareTagButton.clicked.connect(self.show_mifare_results_page)
        self.readMifareTagButton.clicked.connect(self.read_hf_tag)
        self.viewMemoryMifareButton.clicked.connect(self.show_memory_page)
        self.memoryOkButton.clicked.connect(self.show_mifare_options_page)
        self.mifareCloneResultsOkButton.clicked.connect(self.show_mifare_options_page)
        self.cloneMifareButton.clicked.connect(self.clone_mifare_1k_tag)
        self.backButton.clicked.connect(self.show_last_page)
        self.exitButton.clicked.connect(self.exit_app)
        self.basicCommandsButton.clicked.connect(self.show_basic_commands_page)
        self.hwStatusButton.clicked.connect(self.show_results_page)
        self.hwStatusButton.clicked.connect(self.get_hardware_status)
        self.readLFTagButton.clicked.connect(self.show_results_page)
        self.readLFTagButton.clicked.connect(self.search_lf_tag)
        self.readHFTagButton.clicked.connect(self.show_results_page)
        self.readHFTagButton.clicked.connect(self.search_hf_tag)

    def show_connect_proxmark_page(self):
        self.backButton.hide()
        self.topLogoLabel.hide()
        self.actual_page = self.connectProxmarkPage
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

    def show_results_page(self):
        self.backButton.show()
        self.actual_page = self.resultsPage
        self.stackedWidget.setCurrentWidget(self.resultsPage)

    def show_basic_commands_page(self):
        self.backButton.show()
        self.actual_page = self.basicCommandsPage
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.basicCommandsPage)

    def set_results_data(self, successful, title, data, last_page):
        color = "color: rgb(255, 255, 255);"
        if not successful:
            color = "color: rgb(255, 0, 0);"
        self.resultsPageDataLabel.setStyleSheet(color)
        self.resultsPageTitleLabel.setText(title)
        self.resultsPageDataLabel.setTextFormat(Qt.RichText)
        self.resultsPageDataLabel.setWordWrap(True)
        self.resultsPageDataLabel.setText(data)
        self.last_page = last_page

    def start_connection(self):
        connection = self.proxmark.connect_proxmark()
        self.topLogoLabel.show()
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

        if self.actual_page is self.memoryLayoutPage:
            self.memoryLayoutLabel.setText("")
            self.show_mifare_options_page()
        elif self.actual_page is self.mifareResultsPage:
            self.mifareTagResultsLabel.setText("")
            self.show_mifare_options_page()
        elif self.actual_page is self.resultsPage:
            self.resultsPageDataLabel.setText("")
            self.resultsPageTitleLabel.setText("")

        if self.last_page is self.connectProxmarkPage:
            self.topLogoLabel.hide()
            self.show_connect_proxmark_page()
        elif self.last_page is self.mainMenuPage:
            self.show_main_menu_page()
        elif self.last_page is self.mifareOptionsPage:
            self.show_mifare_options_page()
        elif self.last_page is self.basicCommandsPage:
            self.show_basic_commands_page()


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
        result = self.proxmark.read_mifare_hf_tag()
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
        command = "auto"
        result = self.proxmark.execute_command(command)
        title = "TAG INFORMATION"
        # regex = re.compile(r'Valid.*found')
        # match = regex.search(result)
        # if match:
        #     index = match.end()
        #     result = result[:index+1]
        # parsed_result = re.sub(r'\r[\r\n]', r'\r', result)
        data = utils.parse_search_result(result)

        self.set_results_data(True, title, data, self.basicCommandsPage)

    def get_hardware_status(self):
        command = "hw status"
        result = self.proxmark.execute_command(command)
        title = "HARDWARE STATUS"
        data = utils.parse_result(result)
        self.set_results_data(True, title, data, self.basicCommandsPage)

    def search_hf_tag(self):
        command = "hf search"
        result = self.proxmark.execute_command(command)
        title = "HF TAG INFO"
        data = utils.parse_search_result(result)
        self.set_results_data(True, title, data, self.basicCommandsPage)

    def search_lf_tag(self):
        command = "lf search"
        result = self.proxmark.execute_command(command)
        title = "LF TAG INFO"
        data = utils.parse_search_result(result)
        self.set_results_data(True, title, data, self.basicCommandsPage)

    def read_mifare_1k_tag(self):
        result = self.proxmark.execute_command("hf mf autopwn")
        if result:
            files = utils.analyze_result_files(result)
            mifare_tag = Mifare1k(files)
            title = "TAG INFORMATION"
            self.mifareTagResultsLabel.setStyleSheet("color: rgb(255, 255, 255);")
            self.mifareTagResultsLabel.setText(mifare_tag.basic_info())
            self.manage_mifare_tag_information_buttons(True)
            self.last_mifare_tag_read = mifare_tag
        else:
            self.mifareTagResultsLabel.setText("Couldn't read tag")
            self.mifareTagResultsLabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.manage_mifare_tag_information_buttons(False)

    def return_to_connection_page(self):
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)
        self.connectionStatusLabel.setText("")

    def exit_app(self):
        sys.exit()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
