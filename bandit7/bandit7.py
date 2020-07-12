import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit7'
PASSWORD = 'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs'

# initialisation
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connecting to the remote server
print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
stdin, stdout, stderr = client.exec_command('ls -la')
utils.print_stdout(stdout)

# search for the word millionth in data.txt
print('grep millionth data.txt')
_, stdout, _ = client.exec_command('grep millionth data.txt')
utils.print_stdout(stdout)

# based on the output, get the password, which is located next to the word millionth
# using awk
# /millionth/ will perform a regex match,
# print $2 will print the second column of the returned string
print("cat data.txt | awk '/millionth/ {print $2}'")
_, stdout, _ = client.exec_command("cat data.txt | awk '/millionth/ {print $2}'")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit8 password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
print(f"bandit8 password: {password}")

client.close()