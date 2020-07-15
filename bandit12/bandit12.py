import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
# https://pypi.org/project/scp/
import scp

# to execute linux os commands locally
import subprocess

USERNAME = 'bandit12'
PASSWORD = '5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'

if 'data.txt' not in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    # only connect to the remote server if data.txt has not been downloaded
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print('connecting...')
    client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

    print('downloading data.txt...')
    # create an SCP client to download data.txt to work on it on the local machine
    # as this challenge is more complex
    scp_client = scp.SCPClient(client.get_transport(), progress=utils.progress)
    scp_client.get('data.txt')

    # fixed progress printing with print()
    print('\n')
    scp_client.close()
    client.close()
else:
    print("data.txt has been downloaded")

# defining custom print function as it differs from previous levels
def print_out(out):
    print('#' * 50)
    print(out)
    print('#' * 50 + '\n')

# file data.txt
# get the type of data.txt
print('file data.txt')
cmd1 = subprocess.run(['file', 'data.txt'], capture_output=True)
print_out(cmd1.stdout.decode().strip())

# xxd -r data.txt > data2.bin && rm data.txt
# now that we know data.txt is the output of xxd, 
# we can reverse it back to binary using xxd with option r
print('xxd -r data.txt > data2.bin && rm data.txt\n')

# another option is to open a writable file in python and write 
# the output of xxd -r into the opened file
with open('data2.bin', 'w+') as f:
    subprocess.run(['xxd', '-r', 'data.txt'], stdout=f)

# then, we can remove data.txt either using rm command or python's os.remove()
os.remove('data.txt')

# file data2.bin
print('file data2.bin')
cmd3 = subprocess.run(['file', 'data2.bin'], capture_output=True)
print_out(cmd3.stdout.decode().strip())

# mv data2.bin data2.gz && gzip -d data2.gz
# note that gzip needs the input file to have the suffix .gz
print('mv data2.bin data2.gz && gzip -d data2.gz\n')
os.rename('data2.bin', 'data2.gz')

# gzip doesn't produce any output to the stdout
cmd4 = subprocess.run(['gzip', '-d', 'data2.gz'])

# file data2
print('file data2')
cmd5 = subprocess.run(['file', 'data2'], capture_output=True)
print_out(cmd5.stdout.decode().strip())

# bzip2 -d data2
print("bzip2 -d data2")
cmd6 = subprocess.run(['bzip2', '-d', 'data2'], capture_output=True)
print_out(cmd6.stdout.decode().strip())

# file data2.out
print("file data2.out")
cmd7 = subprocess.run(['file', 'data2.out'], capture_output=True)
print_out(cmd7.stdout.decode().strip())

# mv data2.out data4.gz && gzip -d data4.gz
print('mv data2.out data4.gz && gzip -d data4.gz')
os.rename('data2.out', 'data4.gz')
cmd8 = subprocess.run(['gzip', '-d', 'data4.gz'])

# file data4
print('file data4')
cmd9 = subprocess.run(['file', 'data4'], capture_output=True)
print_out(cmd9.stdout.decode().strip())

# tar -xvf data4 && rm data4
print('tar -xvf data4 && rm data4')
cmd10 = subprocess.run(['tar', '-xvf', 'data4'], capture_output=True)
print_out(cmd10.stdout.decode().strip())

os.remove('data4')

# file data5.bin
print('file data5.bin')
cmd11 = subprocess.run(['file', 'data5.bin'], capture_output=True)
print_out(cmd11.stdout.decode().strip())

# tar -xvf data5.bin && rm data5.bin
print('tar -xvf data5.bin && rm data5.bin')
cmd12 = subprocess.run(['tar', '-xvf', 'data5.bin'], capture_output=True)
print_out(cmd12.stdout.decode().strip())
os.remove('data5.bin')

# file data6.bin
print('file data6.bin')
cmd13 = subprocess.run(['file', 'data6.bin'], capture_output=True)
print_out(cmd13.stdout.decode().strip())

# bzip2 -d data6.bin
print("bzip2 -d data6.bin")
cmd14 = subprocess.run(['bzip2', '-d', 'data6.bin'], capture_output=True)
print_out(cmd14.stdout.decode().strip())

# file data6.bin.out
print('file data6.bin.out')
cmd15 = subprocess.run(['file', 'data6.bin.out'], capture_output=True)
print_out(cmd15.stdout.decode().strip())

# tar -xvf data6.bin.out && rm data6.bin.out
print('tar -xvf data6.bin.out && rm data6.bin.out')
cmd16 = subprocess.run(['tar', '-xvf', 'data6.bin.out'], capture_output=True)
print_out(cmd16.stdout.decode().strip())
os.remove('data6.bin.out')

# file data8.bin
print('file data8.bin')
cmd17 = subprocess.run(['file', 'data8.bin'], capture_output=True)
print_out(cmd17.stdout.decode().strip())

# mv data8.bin data8.gz && gzip -d data8.gz
print('mv data8.bin data8.gz && gzip -d data8.gz')
os.rename('data8.bin', 'data8.gz')
cmd18 = subprocess.run(['gzip', '-d', 'data8.gz'])

# file data8
print('file data8')
cmd17 = subprocess.run(['file', 'data8'], capture_output=True)
print_out(cmd17.stdout.decode().strip())

# cat data8 | awk '{print $4}'
# reference: https://stackoverflow.com/questions/295459/how-do-i-use-subprocess-popen-to-connect-multiple-processes-by-pipes
print("cat data8 | awk '{print $4}'")
# send the output to PIPE
cmd18 = subprocess.Popen(['cat', 'data8'], stdout=subprocess.PIPE)
# accept input from PIPE
cmd19 = subprocess.Popen(['awk', '{print $4}'], stdin=cmd18.stdout, stdout=subprocess.PIPE)
# use .communicate() to get the output
# where index 0 is the output of the last command
password = cmd19.communicate()[0].decode().strip()
print_out(password)

os.remove('data8')

# bandit12 password: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
print(f"bandit12 password: {password}")