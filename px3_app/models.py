from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class MfTagsModel(QtCore.QAbstractListModel):
    def __init__(self, tags):
        super().__init__()
        self.tags = tags

    def data(self, index, role) -> str:
        if role == Qt.DisplayRole:
            tag = self.tags[index.row()]
            header = f"Tag {index.row()+1}:"
            if tag.name:
                header += f" {tag.name}"
            body = f"\n{tag.details_short}"
            text = header + body
            return text

    def rowCount(self, index):
        return len(self.tags)
