import time
import string


ADDRESS = 'bandit.labs.overthewire.org'
PORT = 2220
SLEEP = 1


def print_stdout(stdout):
    """
    stdout: obtained from stdout output of paramiko's client.exec_command()\n
    """
    # time.sleep() added as a workaround for known paramiko bug
    # https://github.com/paramiko/paramiko/issues/1617
    time.sleep(SLEEP)

    print("#" * 50)

    for line in stdout:
        line = line.strip('\n')
        print(line)

    print("#" * 50 + '\n')

def print_password(stdout):
    """
    stoud: password returned by the remote server
    """
    time.sleep(SLEEP)

    print("#" * 50)
    
    # remove any whitespaces from the password
    print(f"{stdout.translate('', '', string.whitespace)}")

    print("#" * 50)
