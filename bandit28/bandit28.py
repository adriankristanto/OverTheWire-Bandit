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

# show commit history
print(f'cd /tmp/{FOLDERNAME}/repo && git log -a')
_, stdout, _ = client.exec_command(f'cd /tmp/{FOLDERNAME}/repo && git log -a')
utils.print_stdout(stdout)
# in commit edd935d60906b33f0619605abd1689808ccdd5ee
# they fix an info leak, therefore, we can go to commit 
# c086d11a00c0648d095d04c089786efef5e01264 to see the leaked info

# checkout to commit c086d11a00c0648d095d04c089786efef5e01264
# to see the leaked info
COMMIT = "c086d11a00c0648d095d04c089786efef5e01264"
print(f'cd /tmp/{FOLDERNAME}/repo && git checkout {COMMIT}\n')
_, stdout, _ = client.exec_command(f'cd /tmp/{FOLDERNAME}/repo && git checkout {COMMIT}')

# now, README.md contains the password to bandit29
print(f'cd /tmp/{FOLDERNAME}/repo && cat README.md')
_, stdout, _ = client.exec_command(f'cd /tmp/{FOLDERNAME}/repo && cat README.md')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = stdout[-2].split()[-1]

# bandit29 password: bbc96594b4e001778eee9975372716b2
print(f'bandit29 password: {password}\n')

# cleanup
print('deleting temporary folder...')
_, stdout, _ = client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()