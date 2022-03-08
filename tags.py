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

    def memory_string(self):
        result = ""
        for i in range(16):
            result += f"SECTOR {i}:\n"
            for n in range(4):
                result += f"  {str(n)}: {self.memory[str(i)][str(n)]}\n"
        return result