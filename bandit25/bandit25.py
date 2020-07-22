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

# NOTE: since we will be dealing with 'vi' and 'more', we won't be able to complete
# the challenge programmatically.

# make sure to make the terminal window as small as possible before logging in as bandit26
# this is to prevent the completion of 'more' program
# because 'more' depends on the screen size, if the screen is too small to contain the content of the 
# file, then more will not show everything immediately
# instead, it will wait for user interaction

# next, we can type 'v' to get into an editor while we are still in 'more'
# the editor is set in environment variable EDITOR or VISUAL
# reference: https://man7.org/linux/man-pages/man1/more.1.html

# NOTE: press 'esc' to change to command mode in 'vi'
# it seems that the editor is set to 'vi', therefore, we can use the following commands
# reference: https://people.cs.ksu.edu/~bhoward/vi/vi60.html
# :e to edit another file, which we can use to open /etc/bandit_pass/bandit26
password = '5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z'
print(f'bandit26 password: {password}')
# :set shell=/bin/bash to set the shell to /bin/bash
# :shell to get the shell

bandit26_client.close()

os.remove('bandit26.sshkey')