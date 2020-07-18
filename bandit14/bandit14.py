import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils 

USERNAME = 'bandit14'
PASSWORD = '4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# send the password of the current user (bandit14) to localhost port 30000
print(f"echo {PASSWORD} | nc localhost 30000")
_, stdout, _ = client.exec_command(f"echo {PASSWORD} | nc localhost 30000")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout[1])

# bandit15 password: BfMYroe26WYalil77FoDi9qh59eK5xNr
print(f'bandit15 password: {password}')

client.close()