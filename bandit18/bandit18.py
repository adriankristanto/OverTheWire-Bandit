import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit18'
PASSWORD = 'kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# interestingly, using paramiko doesn't immediately close the SSH connection
# if we login manually, however, the connection will be terminated immediately
# because of "exit 0" at the end of .bashrc
print('cat .bashrc | tail -n2')
_, stdout, _ = client.exec_command('cat .bashrc | tail -n2')
utils.print_stdout(stdout)

# read file readme in the homedirectory
print('cat readme')
_, stdout, _ = client.exec_command('cat readme')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit19 password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
print(f"bandit19 password: {password}")

client.close()