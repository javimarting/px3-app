import pexpect


def connect_proxmark():
    child = pexpect.spawn('pm3', timeout=10, encoding='utf-8')
    result = child.expect(['pm3 -->', pexpect.EOF, pexpect.TIMEOUT])
    print(child.before)
    if result == 0:
        return child
    
    