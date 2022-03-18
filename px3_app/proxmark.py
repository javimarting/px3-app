import pexpect


class Proxmark:
    def __init__(self):
        self.child = None

    def connect_proxmark(self):
        self.child = pexpect.spawn('pm3', timeout=40, encoding='utf-8')
        result = self.child.expect(['pm3 --> ', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.child

    def execute_command(self, command):
        # dev = usb.core.find(idVendor=0x9ac4, idProduct=0x4b8f)
        self.child.sendline(command)
        result = self.child.expect(['pm3 --> ', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.child.before

