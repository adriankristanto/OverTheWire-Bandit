import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils

USERNAME = 'bandit15'
PASSWORD = 'BfMYroe26WYalil77FoDi9qh59eK5xNr'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# send the password of the current user, bandit15, to localhost port 30001 with SSL encryption
# note: -ign_eof helps to open the connection even when the end of file has been reached
# without -ign_eof, we won't be able to do it in one line. We would need to connect first only then we would be able to send the message.
print(f'echo {PASSWORD} | openssl s_client -connect localhost:30001 -ign_eof')
_, stdout, _ = client.exec_command(f'echo {PASSWORD} | openssl s_client -connect localhost:30001 -ign_eof')
stdout = stdout.readlines()
utils.print_stdout(stdout)
password = utils.get_password(stdout[-3])

# bandit16 password: cluFn7wTiGryunymYOu4RcffSxQluehd
print(f'bandit16 password: {password}')

client.close()