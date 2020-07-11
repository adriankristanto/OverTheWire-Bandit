import time


ADDRESS = 'bandit.labs.overthewire.org'
PORT = 2220
SLEEP = 1


def print_stdout(stdout, passwd=0):
    """
    stdout: obtained from stdout output of paramiko's client.exec_command()\n
    passwd: determine whether a password needs to be returned
    """
    password = None

    # time.sleep() added as a workaround for known paramiko bug
    # https://github.com/paramiko/paramiko/issues/1617
    time.sleep(SLEEP)

    print("#" * 50)

    for line in stdout:
        line = line.strip('\n')
        password = line if passwd else None
        print(line)

    print("#" * 50 + '\n')

    return password
