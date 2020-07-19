import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import utils
import paramiko

USERNAME = 'bandit21'
PASSWORD = 'gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)



client.close()