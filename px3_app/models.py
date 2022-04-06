from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from px3_app.utils import ansi_processor


class MfTagsModel(QtCore.QAbstractListModel):
    def __init__(self, tags):
        super().__init__()
        self.tags = tags

    def data(self, index, role):
        if role == Qt.DisplayRole:
            tag = self.tags[index.row()]
            header = f"Tag {index.row()+1}:"
            if tag.name:
                header += f" {tag.name}"
            body = f"\n{tag.get_details_short()}"
            text = header + body
            replacements = {
                f"Tag {index.row()+1}": "yellow",
                "Date": "green",
                "UID": "green",
            }
            # return ansi_processor.replace_with_ansi_color(text, replacements)
            return text

    def rowCount(self, index):
        return len(self.tags)
