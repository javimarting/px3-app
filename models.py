from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class MfTagsModel(QtCore.QAbstractListModel):
    def __init__(self, tags):
        super().__init__()
        self.tags = tags

    def data(self, index, role):
        if role == Qt.DisplayRole:
            tag = self.tags[index.row()]
            return str(tag)

    def rowCount(self, index):
        return len(self.tags)
