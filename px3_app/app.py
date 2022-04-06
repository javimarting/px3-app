#!python3
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

from PyQt5 import QtWidgets

from px3_app.ui.MainWindow import Ui_MainWindow
from px3_app.proxmark import Proxmark
from px3_app.utils import command_output_processor, file_processor, ansi_processor, json_processor
from px3_app.models import MfTagsModel
from px3_app.globals import SAVED_MF_TAGS_DIRECTORY_PATH


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_page = self.connectProxmarkPage
        self.resultsPageButtonContainer.hide()
        self.show_connect_proxmark_page()

        self.proxmark = Proxmark()
        self.mfTagsModel = MfTagsModel(command_output_processor.mf_tags)
        self.mfTagsListView.setModel(self.mfTagsModel)

        self.enter_text_type = ""

        # Connect buttons that change the current page when clicked
        self.backButton.clicked.connect(self.show_last_page)
        self.basicCommandsButton.clicked.connect(self.show_basic_commands_page)
        self.mifare1kButton.clicked.connect(self.show_mifare_options_page)
        self.savedTagsButton.clicked.connect(self.show_mf_saved_tags_page)
        self.customCommandButton.clicked.connect(
            lambda: self.show_enter_text_page("custom command")
        )
        self.mfGiveNameButton.clicked.connect(
            lambda: self.show_enter_text_page("mf tag name")
        )

        # Connect buttons that execute an action when clicked
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
        self.readHFTagButton.clicked.connect(self.show_results_page)
        self.readHFTagButton.clicked.connect(
            lambda: self.run_command("hf search", "HF TAG INFO", self.basicCommandsPage)
        )
        self.mfCloneButton.clicked.connect(self.clone_mf_1k_tag)
        self.mfDeleteButton.clicked.connect(self.delete_mf_1k_tag)
        self.mfSimulateButton.clicked.connect(self.load_mf_1k_tag_to_memory)
        self.startSimulatingButton.clicked.connect(self.simulate_mf_1k_tag)
        self.enterTextButton.clicked.connect(self.enter_text_page_action)
        self.mfInfoButton.clicked.connect(self.get_mf_1k_tag_info)
        self.mfTagsListView.clicked.connect(self.update_give_change_name_button)

# Show different pages
    def show_connect_proxmark_page(self):
        self.backButton.hide()
        self.topLogoLabel.hide()
        self.stackedWidget.setCurrentWidget(self.connectProxmarkPage)

    def show_main_menu_page(self):
        self.backButton.hide()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.mainMenuPage)

    def show_basic_commands_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.basicCommandsPage)

    def show_mifare_options_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareOptionsPage)

    def show_mf_saved_tags_page(self):
        self.mfTagsListView.clearSelection()
        self.last_page = self.mifareOptionsPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareSavedTagsPage)
        self.mfTagsModel.layoutChanged.emit()

    def show_enter_text_page(self, type):
        self.enter_text_type = type
        if type == "custom command":
            self.last_page = self.mainMenuPage
            self.textEdit.setPlaceholderText("Enter command")
            self.enterTextButton.setText("RUN")
        elif type == "mf tag name" and self.get_selected_tag():
            self.last_page = self.mifareSavedTagsPage
            self.textEdit.setPlaceholderText("Enter name")
            self.enterTextButton.setText("DONE")
        self.backButton.show()
        self.stackedWidget.setCurrentWidget(self.enterTextPage)

    def show_custom_command_page(self):
        self.backButton.show()
        self.last_page = self.mainMenuPage
        self.stackedWidget.setCurrentWidget(self.enterTextPage)

    def show_results_page(self):
        self.backButton.show()
        self.stackedWidget.setCurrentWidget(self.resultsPage)

    def show_mf_simulation_page(self):
        self.last_page = self.mifareSavedTagsPage
        self.stackedWidget.setCurrentWidget(self.mifarePage)
        self.mifareStackedWidget.setCurrentWidget(self.mifareSimulatePage)

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
        elif self.last_page is self.enterTextPage:
            self.show_custom_command_page()

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
            error_message = ansi_processor.apply_ansi_color("Couldn't establish connection", "red")
            data = ansi_processor.ansi_to_html(error_message)
            last_page = self.connectProxmarkPage
            self.set_results_data(title, data, last_page)

    def run_command(self, command, title, last_page):
        result = self.proxmark.execute_command(command)
        data = command_output_processor.process_command_output(command, result)
        # print(data)
        self.set_results_data(title, data, last_page)

    # Gets the selected Mifare 1k tag from the mfTagsListView
    def get_selected_tag(self):
        indexes = self.mfTagsListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            mf_tag = self.mfTagsModel.tags[index.row()]
            return mf_tag

    def clone_mf_1k_tag(self):
        tag = self.get_selected_tag()
        if tag:
            eml_file_path = SAVED_MF_TAGS_DIRECTORY_PATH / tag.files['dump_eml_file']
            self.run_command(f"hf mf cload -f {str(eml_file_path)}", "CLONING RESULT", self.mifareSavedTagsPage)

    def load_mf_1k_tag_to_memory(self):
        tag = self.get_selected_tag()
        if tag:
            eml_file_path = SAVED_MF_TAGS_DIRECTORY_PATH / tag.files['dump_eml_file']
            command = f"hf mf eload --1k -f {eml_file_path.relative_to(str(Path.cwd()))}"
            load_memory = self.proxmark.execute_command(command)
            # print(repr(load_memory))
            self.show_mf_simulation_page()
            text = command_output_processor.process_command_output(command, load_memory)
            self.mifareSimulateLabel.setText(text)

    def simulate_mf_1k_tag(self):
        result = self.proxmark.execute_command("hf mf sim --1k -i")
        print("\n")
        print(repr(result))
        if result:
            self.show_mf_saved_tags_page()

    def delete_mf_1k_tag(self):
        tag = self.get_selected_tag()
        if tag:
            file_processor.delete_tag_files(tag.files)
            self.mfTagsModel.tags.remove(tag)
            self.mfTagsModel.layoutChanged.emit()
            self.mfTagsListView.clearSelection()

    def get_mf_1k_tag_info(self):
        tag = self.get_selected_tag()
        if tag:
            title = "MIFARE TAG INFO"
            data = tag.get_details_long()
            self.set_results_data(title, data, self.mifareSavedTagsPage)

    def enter_text_page_action(self):
        if self.enter_text_type == "custom command":
            self.run_custom_command()
        elif self.enter_text_type == "mf tag name":
            self.give_name_to_mf_tag()

    def run_custom_command(self):
        command = self.textEdit.text()
        if command:
            self.run_command(command, "COMMAND RESULT", self.enterTextPage)
            self.textEdit.setText("")

    def give_name_to_mf_tag(self):
        name = self.textEdit.text()
        if name:
            tag = self.get_selected_tag()
            json_file = SAVED_MF_TAGS_DIRECTORY_PATH / tag.files['dump_json_file']
            data = {"Name": name}
            json_processor.add_data_to_json_file(data, json_file)
            tag.name = name
            self.show_mf_saved_tags_page()

    def update_give_change_name_button(self):
        tag = self.get_selected_tag()
        if tag:
            if tag.name:
                self.mfGiveNameButton.setText("CHANGE NAME")
            else:
                self.mfGiveNameButton.setText("GIVE NAME")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
