import utils

class Mifare1k():
    def __init__(self, files):
        self.eml_file = files['eml_file']
        self.json_file = files['json_file']
        self.data = utils.parse_json_file(self.json_file)
        self.uid = self.data['uid']
        self.atqa = self.data['atqa']
        self.sak = self.data['sak']
        self.memory = self.data['memory']

    def basic_info(self):
        return f"UID: {self.uid}\nATQA: {self.atqa}\nSAK: {self.sak}"