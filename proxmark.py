import re
import pexpect
from PyQt5.QtCore import QObject, pyqtSignal

class Proxmark(QObject):
    connected = pyqtSignal(pexpect.pty_spawn.spawn)
    not_connected = pyqtSignal(str)
    successful_operation = pyqtSignal(str)
    unsuccessful_operation = pyqtSignal(str)
    finished = pyqtSignal()

    def connect_proxmark(self):
        self.child = pexpect.spawn('pm3', timeout=30, encoding='utf-8')
        result = self.child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        
        if result == 0:
            self.connected.emit(self.child)
        else:
            self.not_connected.emit("Couldn't establish connection")
        self.finished.emit()
    
    def read_mifare_hf_tag(self):
        self.child.sendline('hf mf autopwn')
        result = self.child.expect(["autopwn execution time", "card select failed"])
        if result == 0:
            return self.child.before
    
    def read_tag(self):
        self.child.sendline('auto')
        self.child.expect('pm3 -->')
        output = self.child.before
        tag_found = re.search(r'Valid .* found', output)
        if tag_found:
            return tag_found.group()
        else:
            return "Couldn't detect tag"




# def connect_proxmark():
#     child = pexpect.spawn('pm3', timeout=10, encoding='utf-8')
#     result = child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
#     print(result)
#     print(child.before)
#     if result == 0:
#         return child
#     else:
#         return None
    
    