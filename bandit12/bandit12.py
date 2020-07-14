import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
# https://pypi.org/project/scp/
import scp

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
    scp_client = scp.SCPClient(client.get_transport())
    scp_client.get('data.txt')

    scp_client.close()
    client.close()
else:
    print("data.txt has been downloaded")


