import re
import pexpect


class Proxmark:
    def __init__(self):
        self.child = None

    def connect_proxmark(self):
        self.child = pexpect.spawn('pm3', timeout=30, encoding='utf-8')
        result = self.child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.child

    def execute_command(self, command):
        self.child.sendline(command)
        result = self.child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        if result == 0:
            return self.child.before

    def read_mifare_hf_tag(self):
        self.child.sendline('hf mf autopwn')
        self.child.expect('pm3 -->')
        output = self.child.before
        result = re.search(r'autopwn execution time', output)
        # result = self.pchild.expect(["autopwn execution time", "card select failed", pexpect.EOF, pexpect.TIMEOUT])
        if result:
            return self.child.before
    
    def read_tag(self):
        self.child.sendline('auto')
        result = self.child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
        response = ""
        if result == 0:
            output = self.child.before
            tag_found = re.search(r'Valid .* found', output)
            if tag_found:
                raw_string = tag_found.group()
                string = re.sub(r"\[32m", "", raw_string)
                response = re.sub(r"\[0m ", "", string)
                return response

    def clone_mifare_1k_tag(self, file):
        print(file)
        command = f"hf mf cload -f {file}"
        self.child.sendline(command)
        self.child.expect('pm3 -->')
        output = self.child.before
        print(output)
        cloned = re.search(r'Done', output)
        if cloned:
            return True


