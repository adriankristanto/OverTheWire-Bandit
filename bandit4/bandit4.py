import sys
import os
# get the path of utils.py, which is stored in the parent directory
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit4'
PASSWORD = 'pIwrPrtPN36QITSp3EQaw936yaFoFgAB'

# initialising
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connecting
print("connecting...\n")
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
stdin, stdout, stderr = client.exec_command('ls -la')
utils.print_stdout(stdout)

print('cd inhere && ls -la')
stdin, stdout, stderr = client.exec_command('cd inhere && ls -la')
utils.print_stdout(stdout)

# references:
# 1. https://unix.stackexchange.com/questions/9619/script-to-list-only-files-of-type-ascii-text-in-the-current-directory
# 2. https://stackoverflow.com/questions/6085156/using-semicolon-vs-plus-with-exec-in-find 
# -type f: finds regular files
# -exec file {} +: execute file command for all found files
# For example, 
# -exec file {} + if we find more than one file, then it will do 'file 1.txt 2.txt ...'
# -exec file {} \; if we find more than one file, then it will do 'file 1.txt; file 2.txt...' 
# the first one is more useful if we want to do something like diff as it will do 
# 'diff 1.txt 2.txt' instead of 'diff 1.txt; 2.txt which would return error'
# and finally, we grep the ones with ASCII as its type
print('find ./inhere -type f -exec file {} + | grep ASCII')
stdin, stdout, stderr = client.exec_command('find ./inhere -type f -exec file {} + | grep ASCII')
utils.print_stdout(stdout)

# read the file with the ASCII type
print('cat ./inhere/-file07')
stdin, stdout, stderr = client.exec_command('cat ./inhere/-file07')

stdout = stdout.readlines()
password = utils.get_password(stdout)
utils.print_stdout(stdout)

# bandit5 password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
print(f'bandit5 password: {password}')

client.close()