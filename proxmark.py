import re
import pexpect
from PyQt5.QtCore import QObject, pyqtSignal

pchild = ""


class Proxmark(QObject):
    connected = pyqtSignal(pexpect.pty_spawn.spawn)
    not_connected = pyqtSignal(str)
    successful_operation = pyqtSignal(str)
    unsuccessful_operation = pyqtSignal(str)
    finished_operation = pyqtSignal(str)
    finished = pyqtSignal()

    def connect_proxmark(self):
        self.pchild = pexpect.spawn('pm3', timeout=30, encoding='utf-8')
        result = self.pchild.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        
        if result == 0:
            self.connected.emit(self.pchild)
        else:
            self.not_connected.emit("Couldn't establish connection")

    def read_mifare_hf_tag(self):
        self.pchild.sendline('hf mf autopwn')
        result = self.pchild.expect(["autopwn execution time", "card select failed", pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.pchild.before
    
    def read_tag(self):
        self.pchild.sendline('auto')
        self.pchild.expect('pm3 -->')
        output = self.pchild.before
        response = ""
        tag_found = re.search(r'Valid .* found', output)
        if tag_found:
            raw_string = tag_found.group()
            string = re.sub(r"\[32m", "", raw_string)
            response = re.sub(r"\[0m ", "", string)
            
        else:
            response = "Couldn't detect tag"
        return response


class Worker(QObject):
    finished = pyqtSignal(str)
    successful = pyqtSignal(str)

    def read_tag(self):
        self.pchild.sendline('auto')
        self.pchild.expect('pm3 -->')
        output = self.pchild.before
        tag_found = re.search(r'Valid .* found', output)
        response = ""
        if tag_found:
            raw_string = tag_found.group()
            string = re.sub(r"\[32m", "", raw_string)
            response = re.sub(r"\[0m ", "", string)
        else:
            response = "Couldn't detect tag"
        self.finished.emit(response)
        

# def connect_proxmark():
#     pchild = pexpect.spawn('pm3', timeout=10, encoding='utf-8')
#     result = pchild.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
#     print(result)
#     print(pchild.before)
#     if result == 0:
#         return pchild
#     else:
#         return None
    
    