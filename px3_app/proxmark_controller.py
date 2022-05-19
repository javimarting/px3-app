import pexpect

from px3_app.globals import ROOT_DIRECTORY


class ProxmarkController:
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
        self.child = pexpect.spawnu('pm3', timeout=40)
        # self.child = pexpect.spawnu('pm3', timeout=40, maxread=4000)
        result = self.child.expect(['pm3 --> ', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            log_file = open(ROOT_DIRECTORY / "log.txt", "w")
            self.child.logfile = log_file
            return self.child

    def execute_command(self, command, stop='pm3 --> '):
        self.child.sendline(command)
        result = self.child.expect_exact([stop, pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            data = self.child.before
            print(f"\n\nCommand: {command}")
            print(f"{data}\n")
            return data

    def simulate_tag(self, tag_path):
        self.child.sendline()

