import paramiko
import utils

USERNAME = 'bandit1'
PASSWORD = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'

# create a new ssh client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to remote server
print('connecting... \n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
stdin, stdout, stderr = client.exec_command('ls -la')

utils.print_stdout(stdout)

# ./- specifies the relative location of the file named -
# this prevents cat from reading from stdin
print('executing cat ./-...')
stdin, stdout, stderr = client.exec_command('cat ./-')

password = utils.print_stdout(stdout, 1)

# bandit2 password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
print('bandit2 password: ' + password)

client.close()