import paramiko
import utils

USERNAME = 'bandit0'
PASSWORD = 'bandit0'

# creating a new ssh client
client = paramiko.SSHClient()

# to prevent unknown host error
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to remote server
print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
stdin, stdout, stderr = client.exec_command('ls -la')
utils.print_stdout(stdout)

# read the password
print('cat readme')
stdin, stdout, stderr = client.exec_command('cat readme')
password = utils.print_stdout(stdout, 1)

# bandit1 password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
print('bandit1 password: ' + password)

client.close()