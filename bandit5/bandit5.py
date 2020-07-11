import sys
import os
# assuming that we run the file from the parent directory, 
# utils.py is in the current directory, so add current directory to the path
# otherwise, add the parent directory to the path
sys.path.insert(1, os.getcwd() if 'utils.py' in os.listdir() else '..')

import paramiko 
import utils

USERNAME = 'bandit5'
PASSWORD = 'koReBOKuIDDepwhWk7jZC0RTdopnAYKh'

# initialisation
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connecting to the remote server
print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
stdin, stdout, stderr = client.exec_command('ls -la')
utils.print_stdout(stdout)

print('cd inhere && ls -la')
stdin, stdout, stderr = client.exec_command('cd inhere && ls -la')
utils.print_stdout(stdout)

# we need a file of size 1033 bytes, which is represented with c in find
# it must not be executable, so, we need ! -executable, where ! means not
# finally, it must be human readable, therefore, we need to use grep ASCII after executing file command
print('find ./inhere -type f -size 1033c ! -executable -exec file {} + | grep ASCII')
stdin, stdout, stderr = client.exec_command('find ./inhere -type f -size 1033c ! -executable -exec file {} + | grep ASCII')
utils.print_stdout(stdout)

# read the file
print('cat ./inhere/maybehere07/.file2')
stdin, stdout, stderr = client.exec_command('cat ./inhere/maybehere07/.file2')

stdout = stdout.readlines()
password = utils.get_password(stdout)
utils.print_stdout(stdout)

# bandit6 password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
print(f"bandit6 password: {password}")

client.close()