

class MifareClassic1k():
    def __init__(self, uid, date, files):
        self.uid = uid
        self.date = date
        self.files = files

    def __str__(self):
        formatted_date = self.date.strftime("%d-%m-%Y %H:%M:%S")
        return f"Tag:\n    Date: {formatted_date}\n    UID: {self.uid}"
