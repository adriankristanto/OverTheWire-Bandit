import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import scp

USERNAME = 'bandit25'
PASSWORD = 'uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())