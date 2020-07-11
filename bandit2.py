import paramiko
import utils

USERNAME = 'bandit2'
PASSWORD = 'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('connecting...\n')
client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

print('ls -la')
stdin, stdout, stderr = client.exec_command('ls -la')

utils.print_stdout(stdout)

# to deal with spaces in a filename in the linux system, 
# we can either wrap the filename in quotes or we can also skip the spaces in the filename
print("cat 'spaces in this filename'")
stdin, stdout, stderr = client.exec_command("cat 'spaces in this filename'")

password = utils.print_stdout(stdout, 1)

# bandit3 password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
print("bandit3 password: " + password)

client.close()