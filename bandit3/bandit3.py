import sys
import os
# get the path of utils.py, which is stored in the parent directory
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit3'
PASSWORD = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'

# initialising
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connecting
print("connecting...\n")
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print("ls -la")
stdin, stdout, stderr = client.exec_command('ls -la')
utils.print_stdout(stdout)

# to list out hidden files, we can use the option a for ls
print("cd inhere && ls -la")
stdin, stdout, stderr = client.exec_command('cd inhere && ls -la')
utils.print_stdout(stdout)

# read the hidden file
print('cat ./inhere/.hidden')
stdin, stdout, stderr = client.exec_command('cat ./inhere/.hidden')

stdout = stdout.readlines()
password = utils.get_password(stdout)
utils.print_stdout(stdout)

# bandit4 password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
print(f'bandit4 password: {password}')

client.close()