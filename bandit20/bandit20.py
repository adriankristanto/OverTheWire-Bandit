import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit20'
PASSWORD = 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j'

client1 = paramiko.SSHClient()
client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client1.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)
client2.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

client1.close()
client2.close()