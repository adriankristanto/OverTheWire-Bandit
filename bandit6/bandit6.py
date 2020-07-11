import sys
import os
# assuming that we run the file from the parent directory, 
# utils.py is in the current directory, so add current directory to the path
# otherwise, add the parent directory to the path
sys.path.insert(1, os.getcwd() if 'utils.py' in os.listdir() else '..')

import paramiko
import utils

USERNAME = 'bandit6'
PASSWORD = 'DXjZPULLxYr17uwoI01bNLQbtFemEgo7'

# initialisation
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# the password is stored somewhere on the server, therefore, we don't need to do ls -la
print("find / -type f -user bandit7 -group bandit6 -exec file {} + | grep ASCII")
stdin, stdout, stderr = client.exec_command("find / -type f -user bandit7 -group bandit6 -exec file {} + | grep ASCII")
utils.print_stdout(stdout)

print("cat /var/lib/dpkg/info/bandit7.password")
stdin, stdout, stderr = client.exec_command("cat /var/lib/dpkg/info/bandit7.password")

stdout = stdout.readlines()
password = utils.get_password(stdout)
utils.print_stdout(stdout)

# bandit7 password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
print(f"bandit7 password: {password}")