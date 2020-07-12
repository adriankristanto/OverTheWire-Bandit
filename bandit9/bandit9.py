import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit9'
PASSWORD = 'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print("strings data.txt | awk '/=+/'")
# with data.txt is stored in the same location, we don't need to perform ls -la
# firstly, the password is stored in the line that is human-readable, therefore, we can use strings to achieve this
# next, we know that the password is preceded with one or more =, therefore, we can use awk to achieve this
# note that the line doesn't necessarily start with =
_, stdout, _ = client.exec_command("strings data.txt | awk '/=+/'")
utils.print_stdout(stdout)

print("strings data.txt | awk '/=+ /' | tail -n1 | awk '{print $2}'")
# from the output, we can see that the password is preceded by multiple = and a space, therefore, we can improve the 
# regex to get the password
# also note that the password is the last line preceded with = and a space, so we can use tail -n1
# since the password is located at the second column, we can get the password with awk
_, stdout, _ = client.exec_command("strings data.txt | awk '/=+ /' | tail -n1 | awk '{print $2}'")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit10 password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
print(f"bandit10 password: {password}")

client.close()