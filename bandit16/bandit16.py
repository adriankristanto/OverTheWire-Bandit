import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import utils
import paramiko

USERNAME = 'bandit16'
PASSWORD = 'cluFn7wTiGryunymYOu4RcffSxQluehd'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting as bandit16...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

# we use nmap to determine the open port in range 31000 to 32000
# here, we use -sV to detect service running on the port
# _, stdout, _ = client.exec_command('nmap -sV -p31000-32000 localhost')
# utils.print_stdout(stdout)

# based on the output, we can see that 2 ports are speaking SSL, which are 31518 and 31790
# however, we know that 31518 runs echo, so, we want to avoid that as it will only 
# echo back what we send to it
# therefore, we need to connect to port 31790
_, stdout, _ = client.exec_command(f'echo {PASSWORD} | openssl s_client -connect localhost:31790 -ign_eof')
stdout = stdout.readlines()
utils.print_stdout(stdout)

client.close()

# write the private key file of bandit17
start = stdout.index('-----BEGIN RSA PRIVATE KEY-----\n')
end = stdout.index('-----END RSA PRIVATE KEY-----\n')
with open('sshkey.private', 'w') as f:
    for lines in stdout[start:end]:
        f.write(lines)
    f.write(stdout[end].strip())

# change the permission of the private key
# otherwise, the permission would be too open
# and an error would occur
os.chmod('sshkey.private', 0o600)

bandit17_client = paramiko.SSHClient()
bandit17_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connecting as bandit17
print('connecting as bandit17...\n')
key=paramiko.RSAKey.from_private_key_file('sshkey.private')
bandit17_client.connect(hostname=utils.ADDRESS, port=utils.PORT, username='bandit17', pkey=key)

# read the password from /etc/bandit_pass/bandit17
_, stdout, _ = bandit17_client.exec_command('cat /etc/bandit_pass/bandit17')
utils.print_stdout(stdout)

bandit17_client.close()

os.remove('sshkey.private')