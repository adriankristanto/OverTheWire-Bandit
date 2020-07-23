import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time
import uuid

USERNAME = 'bandit31'
PASSWORD = '47e603bb428404d265f59c42920d81e5'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

FOLDERNAME = str(uuid.uuid4())
REPONAME = 'ssh://bandit31-git@localhost/home/bandit31-git/repo'
print(f'folder name: {FOLDERNAME}\n')

print(f'mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}')
stdin, stdout, _ = client.exec_command(f'mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}', get_pty=True)
stdin.write('yes\n')
time.sleep(1)
stdin.write(f'{PASSWORD}\n')
stdin.flush()
utils.print_stdout(stdout)

# cleanup
print('deleting temporary directory...')
client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()