import pexpect

from px3_app.globals import ROOT_DIRECTORY


class ProxmarkClient:
    """A class that represents the Proxmark Client.

    Attributes:
        child (pexpect.pty_spawn.spawn): Child process.

    Methods:
        connect_proxmark()
        execute_command(command)

    """

    def __init__(self, child=None):
        self.child = child

    def connect_proxmark(self):
        self.child = pexpect.spawn('pm3', timeout=40, encoding='utf-8')
        result = self.child.expect(['pm3 --> ', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            log_file = open(ROOT_DIRECTORY / "log.txt", "w")
            self.child.logfile = log_file
            return self.child

    def execute_command(self, command):
        self.child.sendline(command)
        result = self.child.expect(['pm3 --> ', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            data = self.child.before
            return data

