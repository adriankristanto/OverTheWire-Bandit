import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time
import uuid

USERNAME = 'bandit30'
PASSWORD = '5b90576bedb2cc04c86a9e924ce42faf'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

FOLDERNAME = str(uuid.uuid4())
REPONAME = 'ssh://bandit30-git@localhost/home/bandit30-git/repo'
print(f"folder name: {FOLDERNAME}\n")

print(f"mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}")
stdin, stdout, _ = client.exec_command(f"mkdir /tmp/{FOLDERNAME} && cd /tmp/{FOLDERNAME} && git clone {REPONAME}", get_pty=True)
stdin.write('yes\n')
time.sleep(1)
stdin.write(f'{PASSWORD}\n')
stdin.flush()
utils.print_stdout(stdout)

# note that packed refs contains all mapping to branches and tags of a git repo
# reference: https://www.atlassian.com/git/tutorials/refs-and-the-reflog#packed-refs
"""
This moves all of the individual branch and tag files in the refs folder 
into a single file called packed-refs located in the top of the .git directory. 
If you open up this file, you’ll find a mapping of commit hashes to refs
"""
print(f'cat /tmp/{FOLDERNAME}/repo/.git/packed-refs')
_, stdout, _ = client.exec_command(f'cat /tmp/{FOLDERNAME}/repo/.git/packed-refs')
utils.print_stdout(stdout)

# we can see that there is a tag called secret
# we can tag the commit hash and use git show to show the content
_, stdout, _ = client.exec_command(f'cd /tmp/{FOLDERNAME}/repo && git show f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout[0])

# bandit31 password: 47e603bb428404d265f59c42920d81e5
print(f'bandit31 password: {password}\n')

# clean up
print('deleting temporary directory...')
client.exec_command(f'rm -rf /tmp/{FOLDERNAME}')

client.close()