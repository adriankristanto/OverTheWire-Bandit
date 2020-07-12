import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit10'
PASSWORD = 'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('base64 -d data.txt')
# we know that the data is base64 encoded
_, stdout, _ = client.exec_command('base64 -d data.txt')
utils.print_stdout(stdout)

print("base64 -d data.txt | awk '{print $4}'")
_, stdout, _ = client.exec_command("base64 -d data.txt | awk '{print $4}'")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit11 password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
print(f"bandit11 password: {password}")

client.close()