from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class MfTagsModel(QtCore.QAbstractListModel):
    def __init__(self, tags):
        super().__init__()
        self.tags = tags

    def data(self, index, role):
        if role == Qt.DisplayRole:
            tag = self.tags[index.row()]
            text = f"Tag {index.row()+1}:\n{str(tag)}"
            return text

    def rowCount(self, index):
        return len(self.tags)
