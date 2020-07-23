import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time
import uuid

USERNAME = 'bandit29'
PASSWORD = 'bbc96594b4e001778eee9975372716b2'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

FOLDERNAME = str(uuid.uuid4())
REPONAME = 'ssh://bandit29-git@localhost/home/bandit29-git/repo'
print(f'folder name: {FOLDERNAME}\n')

print(f"mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}")
stdin, stdout, _ = client.exec_command(f"mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}", get_pty=True)
stdin.write('yes\n')
time.sleep(1)
stdin.write(PASSWORD + '\n')
stdin.flush()
utils.print_stdout(stdout)

# clean up
print('deleting temporary directory...')
client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()