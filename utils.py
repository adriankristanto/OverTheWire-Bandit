import time
import string
import sys


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


def get_password(stdout):
    """
    stoud: password returned by the remote server
    """
    time.sleep(SLEEP)

    password = ''

    # remove any whitespaces from the password
    # reference: https://stackoverflow.com/questions/3739909/how-to-strip-all-whitespace-from-string
    password = ''.join(stdout).strip('\n').translate(str.maketrans('', '', string.whitespace))

    return password


# scp util progress
# reference: https://github.com/jbardin/scp.py
def progress(filename, size, sent):
    sys.stdout.write(f"{filename.decode()} progress: {float(sent) / float(size) * 100:.2f}%\r")