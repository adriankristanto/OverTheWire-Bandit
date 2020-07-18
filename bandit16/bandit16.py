import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import utils
import paramiko

USERNAME = 'bandit16'
PASSWORD = 'cluFn7wTiGryunymYOu4RcffSxQluehd'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# we use nmap to determine the open port in range 31000 to 32000
# here, we use -sV to detect service running on the port
_, stdout, _ = client.exec_command('nmap -sV -p31000-32000 localhost')
utils.print_stdout(stdout)

# based on the output, we can see that 2 ports are speaking SSL, which are 31518 and 31790
# however, we know that 31518 runs echo, so, we want to avoid that as it will only 
# echo back what we send to it
# therefore, we need to connect to port 31790
_, stdout, _ = client.exec_command(f'echo {PASSWORD} | openssl s_client -connect localhost:31790 -ign_eof')
stdout = stdout.readlines()
utils.print_stdout(stdout)
print(stdout)

client.close()