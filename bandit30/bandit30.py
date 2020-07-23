import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time
import uuid

USERNAME = 'bandit30'
PASSWORD = '5b90576bedb2cc04c86a9e924ce42faf'

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

FOLDERNAME = str(uuid.uuid4())
REPONAME = 'ssh://bandit30-git@localhost/home/bandit30-git/repo'
print(f"folder name: {FOLDERNAME}\n")

stdin, stdout, _ = client.exec_command(f"mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}")
stdin.write('yes\n')
time.sleep(1)
stdin.write(f'{PASSWORD}\n')
stdin.flush()
utils.print_stdout(stdout)

# clean up
print('deleting temporary directory...')
client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()