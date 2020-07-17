import sys
import os
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import scp 
import paramiko
import utils

USERNAME = 'bandit13'
PASSWORD = '8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

scp_client = scp.SCPClient(client.get_transport(), progress=utils.progress)
scp_client.get('sshkey.private')

print('\n')

scp_client.close()
client.close()

os.remove('sshkey.private')