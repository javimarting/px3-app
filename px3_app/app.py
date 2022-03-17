#!python3

import sys
import os

from PyQt5 import QtWidgets

from px3_app.ui.MainWindow import Ui_MainWindow
from px3_app.proxmark import Proxmark
from px3_app.utils import command_output_processor
from px3_app.models import MfTagsModel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_page = self.connectProxmarkPage
        self.show_connect_proxmark_page()

        self.proxmark = Proxmark()
        self.mfTagsModel = MfTagsModel(command_output_processor.mf_tags)
        self.mfTagsListView.setModel(self.mfTagsModel)

        # Connect buttons that change the current page
        self.backButton.clicked.connect(self.show_last_page)
        self.basicCommandsButton.clicked.connect(self.show_basic_commands_page)
        self.mifare1kButton.clicked.connect(self.show_mifare_options_page)
        self.savedTagsButton.clicked.connect(self.show_mf_saved_tags_page)
        self.customCommandButton.clicked.connect(self.show_custom_command_page)

        # Connect buttons that execute an action
        self.exitButton.clicked.connect(exit)
        self.connectProxmarkButton.clicked.connect(self.start_connection)
        self.autoDetectTagButton.clicked.connect(
            lambda: self.run_command("auto", "TAG INFO", self.basicCommandsPage)
        )
        self.mfAutopwnButton.clicked.connect(
            lambda: self.run_command("hf mf autopwn", "AUTOPWN INFO", self.mifareOptionsPage)
        )

        self.hwStatusButton.clicked.connect(
            lambda: self.run_command("hw status", "HARDWARE STATUS", self.basicCommandsPage)
        )
        self.readLFTagButton.clicked.connect(
            lambda: self.run_command("lf search", "LF TAG INFO", self.basicCommandsPage)
        )
        self.readHFTagButton.clicked.connect(
            lambda: self.run_command("hf search", "HF TAG INFO", self.basicCommandsPage)
        )
        self.mfCloneButton.clicked.connect(self.clone_mf_1k_tag)
        self.mfDeleteButton.clicked.connect(self.delete_mf_1k_tag)
        self.mfSimulateButton.clicked.connect(self.load_mf_1k_tag_to_memory)
        self.startSimulatingButton.clicked.connect(self.simulate_mf_1k_tag)
        self.runCommandButton.clicked.connect(self.run_custom_command)
        self.mfInfoButton.clicked.connect(self.get_mf_1k_tag_info)

# Show different pages
    def show_connect_proxmark_page(self):
        self.backButton.hide()
        self.topLogoLabel.hide()
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

    def show_results_page(self):
        self.backButton.show()
        self.stackedWidget.setCurrentWidget(self.resultsPage)

    def show_basic_commands_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.basicCommandsPage)

    def show_custom_command_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.customCommandPage)

    def show_last_page(self):
        if self.stackedWidget.currentWidget() is self.resultsPage:
            self.resultsPageDataLabel.setText("")
            self.resultsPageTitleLabel.setText("")
        elif self.stackedWidget.currentWidget() is self.mifareStackedWidget and \
                self.mifareStackedWidget.currentWidget() is self.mifareSimulatePage:
            self.mifareSimulateLabel.setText("")

        if self.last_page is self.connectProxmarkPage:
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

    def show_main_menu_page(self):
        self.backButton.hide()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)
    
    def show_mifare_options_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareOptionsPage)

    def show_mf_saved_tags_page(self):
        self.last_page = self.mifareOptionsPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareSavedTagsPage)

    def show_mf_simulation_page(self):
        self.last_page = self.mifareSavedTagsPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareSimulatePage)

# Actions
    def set_results_data(self, title, data, last_page):
        self.resultsPageTitleLabel.setText(title)
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
            data = command_output_processor.generate_error_message("Couldn't establish connection")
            last_page = self.connectProxmarkPage
            self.set_results_data(title, data, last_page)

    def run_command(self, command, title, last_page):
        result = self.proxmark.execute_command(command)
        data = command_output_processor.process_command_output(result)
        self.set_results_data(title, data, last_page)

    def get_selected_tag(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            self.mfTagsListView.clearSelection()
            return mf_tag

    def clone_mf_1k_tag(self):
        tag = self.get_selected_tag()
        if tag:
            self.run_command(f"hf mf cload -f {tag.files['dump_eml_file']}", "CLONING RESULT", self.mifareSavedTagsPage)

    def load_mf_1k_tag_to_memory(self):
        tag = self.get_selected_tag()
        if tag:
            load_memory = self.proxmark.execute_command(f"hf mf eload --1k -f {tag.files['dump_eml_file']}")
            self.show_mf_simulation_page()
            text = command_output_processor.process_command_output(load_memory)
            self.mifareSimulateLabel.setText(text)

    def simulate_mf_1k_tag(self):
        result = self.proxmark.execute_command("hf mf sim --1k -i")
        self.show_mf_saved_tags_page()

    def delete_mf_1k_tag(self):
        tag = self.get_selected_tag()
        if tag:
            for k, v in tag.files.items():
                try:
                    os.remove(v)
                except:
                    pass
            self.mfTagsModel.tags.remove(tag)
            self.mfTagsModel.layoutChanged.emit()
            self.mfTagsListView.clearSelection()

    def get_mf_1k_tag_info(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            title = "MIFARE TAG INFO"
            data = mf_tag.get_details_long()
            self.set_results_data(title, data, self.mifareSavedTagsPage)

    def run_custom_command(self):
        command = self.commandEdit.text()
        if command:
            self.run_command(command, "COMMAND RESULT", self.customCommandPage)
            self.commandEdit.setText("")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
