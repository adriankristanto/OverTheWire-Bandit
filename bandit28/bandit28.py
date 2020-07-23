import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import uuid
import time

USERNAME = "bandit28"
PASSWORD = "0ef186ac70e04ea33b4c1853d2526fa2"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

FOLDERNAME = uuid.uuid4()
REPONAME = 'ssh://bandit28-git@localhost/home/bandit28-git/repo'

print(f'folder name: {FOLDERNAME}\n')
print(f'mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}')
stdin, stdout, _ = client.exec_command(f'mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}', get_pty=True)
# Are you sure you want to continue connecting (yes/no)?
stdin.write('yes\n')
time.sleep(1)
stdin.write(PASSWORD + '\n')
stdin.flush()
utils.print_stdout(stdout)

print(f'cd /tmp/{FOLDERNAME} && git log -a')
_, stdout, _ = client.exec_command(f'cd /tmp/{FOLDERNAME} && git log -a')
utils.print_stdout(stdout)

# cleanup
print('deleting temporary folder...')
_, stdout, _ = client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()