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

# download the private key of bandit14
scp_client = scp.SCPClient(client.get_transport(), progress=utils.progress)
scp_client.get('sshkey.private')

print('\n')

scp_client.close()
client.close()

# connecting as bandit14 using the downloaded ssh private key
bandit14_client = paramiko.SSHClient()
bandit14_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# reference: https://stackoverflow.com/questions/54612609/paramiko-not-a-valid-rsa-private-key-file
privatekey = paramiko.RSAKey.from_private_key_file('sshkey.private')
bandit14_client.connect(hostname=utils.ADDRESS, port=utils.PORT, username='bandit14', pkey=privatekey)

print('cat /etc/bandit_pass/bandit14')
# read bandit14 password stored in /etc/bandit_pass/bandit14
_, stdout, _ = bandit14_client.exec_command('cat /etc/bandit_pass/bandit14')
utils.print_stdout(stdout)

bandit14_client.close()
os.remove('sshkey.private')