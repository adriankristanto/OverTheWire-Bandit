import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import scp

USERNAME = 'bandit25'
PASSWORD = 'uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting as bandit25...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# get the shell used by bandit26
# as it is not /bin/bash
print('cat /etc/passwd | grep bandit26')
_, stdout, _ = client.exec_command('cat /etc/passwd | grep bandit26')
utils.print_stdout(stdout)

# as we can see, bandit26 uses /usr/bin/showtext as its shell
print('cat /usr/bin/showtext')
_, stdout, _ = client.exec_command('cat /usr/bin/showtext')
utils.print_stdout(stdout)

# the shell will execute the 'more' command
# which will show the content of the file based on the screen size
# e.g. if the screen size is small, then it won't show all of the content
# but part by part where each part will fit the screen size of user

# download private key of bandit26
print('downloading bandit26 private key file...\n')
scp_client = scp.SCPClient(client.get_transport(), progress=utils.progress)
scp_client.get('bandit26.sshkey')
print('\n')

scp_client.close()

client.close()

bandit26_client = paramiko.SSHClient()
bandit26_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting as bandit26...\n')
key = paramiko.RSAKey.from_private_key_file('bandit26.sshkey')
bandit26_client.connect(hostname=utils.ADDRESS, port=utils.PORT, username='bandit26', pkey=key)

bandit26_client.close()

os.remove('bandit26.sshkey')