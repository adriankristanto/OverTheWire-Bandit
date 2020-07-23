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

client.close()