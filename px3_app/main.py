import sys

from PyQt5.QtWidgets import QApplication

from px3_app.main_controller import MainController


def main():
    app = QApplication(sys.argv)
    window = MainController()
    window.show()
    app.exec_()


main()
