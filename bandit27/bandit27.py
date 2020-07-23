import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import uuid
import time

USERNAME = 'bandit27'
PASSWORD = '3ba3118a22e93127a4ed485be72ef5ea'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

FOLDERNAME = str(uuid.uuid4())
print(f'folder name: {FOLDERNAME}\n')
REPONAME = 'ssh://bandit27-git@localhost/home/bandit27-git/repo'

# reference: https://stackoverflow.com/questions/6270677/how-to-run-sudo-with-paramiko-python
print(f'mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}')
# get_pty to get the prompt to insert password
stdin, stdout, _ = client.exec_command(f'mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}', get_pty=True)
# Are you sure you want to continue connecting (yes/no)?
stdin.write('yes\n')
time.sleep(1)
# insert the password to clone the git repo
stdin.channel.send(PASSWORD + '\n')
stdin.flush()
utils.print_stdout(stdout)

# move to the repo and read the readme file
print(f'cd /tmp/{FOLDERNAME}/repo && cat README')
_, stdout, _ = client.exec_command(f'cd /tmp/{FOLDERNAME}/repo && cat README')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout[0].split()[-1])

# bandit28 password: 0ef186ac70e04ea33b4c1853d2526fa2
print(f'bandit28 password: {password}\n')

# cleanup
print('deleting temporary folder...')
_, stdout, _ = client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()