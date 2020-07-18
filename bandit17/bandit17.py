import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import utils
import paramiko

USERNAME = 'bandit17'
PASSWORD = 'xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# get the difference between passwords.old and passwords.new
# since there is only one line difference between passwords.old and passwords.new
# and passwords.new is the second argument of diff command,
# bandit18 password will be displayed in the last line
# therefore, we can use tail -n1 to get the password
# since the output is '> (password)', we can use awk to get the second column that contains the password
print("diff passwords.old passwords.new | tail -n1 | awk '{print $2}'")
_, stdout, _ = client.exec_command("diff passwords.old passwords.new | tail -n1 | awk '{print $2}'")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit18 password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
print(f'bandit18 password: {password}')

client.close()