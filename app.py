#!python3

import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from MainWindow import Ui_MainWindow
from proxmark import Proxmark
import utils
from models import MfTagsModel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_page = self.connectProxmarkPage
        self.actual_page = self.connectProxmarkPage
        self.backButton.hide()
        self.topLogoLabel.hide()

        self.proxmark = Proxmark()
        self.mfTagsModel = MfTagsModel(utils.mf_tags)
        self.mfTagsListView.setModel(self.mfTagsModel)

        self.last_mifare_tag_read = None

        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

        self.connectProxmarkButton.clicked.connect(self.start_connection)
        self.autoDetectTagButton.clicked.connect(self.read_tag)
        self.mifare1kButton.clicked.connect(self.show_mifare_options_page)
        self.mfAutopwnButton.clicked.connect(self.read_mf_1k_tag)
        self.backButton.clicked.connect(self.show_last_page)
        self.exitButton.clicked.connect(self.exit_app)
        self.basicCommandsButton.clicked.connect(self.show_basic_commands_page)
        self.hwStatusButton.clicked.connect(self.get_hardware_status)
        self.readLFTagButton.clicked.connect(self.search_lf_tag)
        self.readHFTagButton.clicked.connect(self.search_hf_tag)
        self.savedTagsButton.clicked.connect(self.show_mf_saved_tags_page)
        self.mfCloneButton.clicked.connect(self.clone_mf_1k_tag)
        self.mfDeleteButton.clicked.connect(self.delete_mf_1k_tag)
        self.mfSimulateButton.clicked.connect(self.load_mf_1k_tag_to_memory)
        self.startSimulatingButton.clicked.connect(self.simulate_mf_1k_tag)
        self.customCommandButton.clicked.connect(self.show_custom_command_page)
        self.runCommandButton.clicked.connect(self.run_custom_command)
        self.mfInfoButton.clicked.connect(self.get_mf_1k_tag_info)

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

    def show_custom_command_page(self):
        self.backButton.show()
        self.actual_page = self.customCommandPage
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.customCommandPage)

    def set_results_data(self, successful, title, data, last_page):
        color = "color: rgb(255, 255, 255);"
        if not successful:
            color = "color: rgb(255, 0, 0);"
        self.resultsPageDataLabel.setStyleSheet(color)
        self.resultsPageTitleLabel.setText(title)
        self.resultsPageDataLabel.setWordWrap(True)
        self.resultsPageDataLabel.setText(data)
        self.last_page = last_page
        self.show_results_page()

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

        if self.actual_page is self.resultsPage:
            self.resultsPageDataLabel.setText("")
            self.resultsPageTitleLabel.setText("")
        elif self.actual_page is self.mifareSimulatePage:
            self.mifareSimulateLabel.setText("")


        if self.last_page is self.connectProxmarkPage:
            self.topLogoLabel.hide()
            self.show_connect_proxmark_page()
        elif self.last_page is self.mainMenuPage:
            self.show_main_menu_page()
        elif self.last_page is self.mifareOptionsPage:
            self.show_mifare_options_page()
        elif self.last_page is self.basicCommandsPage:
            self.show_basic_commands_page()
        elif self.last_page is self.mifareSavedTagsPage:
            self.show_mf_saved_tags_page()
        elif self.last_page is self.customCommandPage:
            self.show_custom_command_page()

        self.actual_page = self.last_page

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

    def show_mf_saved_tags_page(self):
        self.last_page = self.mifareOptionsPage
        self.actual_page = self.mifareSavedTagsPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareSavedTagsPage)

    def show_mf_simulation_page(self):
        self.last_page = self.mifareSavedTagsPage
        self.actual_page = self.mifareSimulatePage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareSimulatePage)

    def read_tag(self):
        command = "auto"
        result = self.proxmark.execute_command(command)
        title = "TAG INFORMATION"
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

    def read_mf_1k_tag(self):
        result = self.proxmark.execute_command("hf mf autopwn")
        if result:
            title = "MIFARE TAG INFO"
            data = utils.parse_mf_1k_result(result)
            self.set_results_data(True, title, data, self.mifareOptionsPage)

            self.mfTagsModel.layoutChanged.emit()

    def clone_mf_1k_tag(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            result = self.proxmark.execute_command(f"hf mf cload -f {mf_tag.files['dump_eml_file']}")
            title = "CLONING RESULT"
            data = utils.parse_result(result)
            self.set_results_data(True, title, data, self.mifareSavedTagsPage)
            self.mfTagsListView.clearSelection()

    def load_mf_1k_tag_to_memory(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            load_memory = self.proxmark.execute_command(f"hf mf eload --1k -f {mf_tag.files['dump_eml_file']}")
            self.show_mf_simulation_page()
            text = utils.parse_result(load_memory)
            self.mifareSimulateLabel.setText(text)

    def simulate_mf_1k_tag(self):
        result = self.proxmark.execute_command("hf mf sim --1k -i")
        self.show_mf_saved_tags_page()

    def delete_mf_1k_tag(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            for k, v in mf_tag.files.items():
                try:
                    os.remove(v)
                except:
                    pass
            del self.mfTagsModel.tags[index.row()]
            self.mfTagsModel.layoutChanged.emit()
            self.mfTagsListView.clearSelection()

    def get_mf_1k_tag_info(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            title = "MIFARE TAG INFO"
            data = mf_tag.get_basic_info()
            print(data)
            self.set_results_data(True, title, data, self.mifareSavedTagsPage)

    def run_custom_command(self):
        command = self.commandEdit.text()
        if command:
            result = self.proxmark.execute_command(command)
            title = "COMMAND RESULT"
            data = utils.parse_result(result)
            self.set_results_data(True, title, data, self.customCommandPage)
            self.commandEdit.setText("")

    def exit_app(self):
        sys.exit()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
