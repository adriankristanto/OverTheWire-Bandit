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
    print()
    scp_client.close()
    client.close()
else:
    print("data.txt has been downloaded")

# file data.txt
# get the type of data.txt
print('file data.txt')
cmd1 = subprocess.run(['file', 'data.txt'], capture_output=True)
print(cmd1.stdout.decode().strip())

# xxd -r data.txt > data2.bin && rm data.txt
# now that we know data.txt is the output of xxd, 
# we can reverse it back to binary using xxd with option r
print('xxd -r data.txt > data2.bin && rm data.txt')

# another option is to open a writable file in python and write 
# the output of xxd -r into the opened file
with open('data2.bin', 'w+') as f:
    subprocess.run(['xxd', '-r', 'data.txt'], stdout=f)

# then, we can remove data.txt either using rm command or python's os.remove()
os.remove('data.txt')

# file data2.bin
print('file data2.bin')
cmd3 = subprocess.run(['file', 'data2.bin'], capture_output=True)
print(cmd3.stdout.decode().strip())

# mv data2.bin data2.gz && gzip -d data2.gz
# file data2
# bzip2 -d data2
# file data2.out
# mv data2.out data4.gz && gzip -d data4.gz
# file data4
# tar -xvf data4 && rm data4
# file data5.bin
# tar -xvf data5.bin && rm data5.bin
# file data6.bin
# bzip2 -d data6.bin
# file data6.bin.out
# tar -xvf data6.bin.out && rm data6.bin.out
# file data8.bin
# mv data8.bin data8.gz && gzip -d data8.gz
# file data8
# cat data8

# The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL