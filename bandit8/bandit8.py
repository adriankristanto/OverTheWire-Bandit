import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit8'
PASSWORD = 'cvX2JJa4CFALtqS87jk27qwqGhBM9plV'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
_, stdout, _ = client.exec_command('ls -la')
utils.print_stdout(stdout)

# to get the unique line, before passing the data to uniq command, we need to sort it first
# this is because uniq will only consider the adjacent lines to determine whether a line is unique
# for example, given 4 lines AABA, the unique line supposed to be B, but uniq will see this as 
# 2 A, 1 B and 1 A, therefore, the B and the last A are considered as unique lines
# to confirm that the line we get is unique, we can pass in option c to uniq command to get the how many 
# times the line appeared in the text
print('cat data.txt | sort | uniq -uc')
_, stdout, _ = client.exec_command('cat data.txt | sort | uniq -uc')
utils.print_stdout(stdout)

# to get the password, we can pass the option u to uniq command to print only the unique line
print('cat data.txt | sort | uniq -u')
_, stdout, _ = client.exec_command('cat data.txt | sort | uniq -u')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit9 password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
print(f'bandit9 password: {password}')

client.close()
