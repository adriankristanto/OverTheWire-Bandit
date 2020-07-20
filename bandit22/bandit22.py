import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import utils
import paramiko

USERNAME = 'bandit22'
PASSWORD = 'Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())