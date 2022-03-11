import re
import pexpect


class Proxmark:
    def __init__(self):
        self.child = None

    def connect_proxmark(self):
        self.child = pexpect.spawn('pm3', timeout=40, encoding='utf-8')
        result = self.child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.child

    def execute_command(self, command):
        self.child.sendline(command)
        result = self.child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.child.before
