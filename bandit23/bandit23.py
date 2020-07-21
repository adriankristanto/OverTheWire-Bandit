import os
import sys
sys.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit23'
PASSWORD = 'jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -l /etc/cron.d/')

print('cat /etc/cron.d/cronjob_bandit24')
# note that according to https://crontab.guru/#*_*_*_*_*
"""
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
"""
# the cronjob is executed every minute

print('cat /usr/bin/cronjob_bandit24.sh')

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

client.close()