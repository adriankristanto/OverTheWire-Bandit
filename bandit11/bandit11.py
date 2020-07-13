import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit11'
PASSWORD = 'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
# performing ROT13 with tr
_, stdout, _ = client.exec_command("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
utils.print_stdout(stdout)

print("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | awk '{print $4}'")
_, stdout, _ = client.exec_command("cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m' | awk '{print $4}'")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit12 password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
print(f"bandit12 password: {password}")

client.close()