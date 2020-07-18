import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/..')

import paramiko
import utils
import time

import multiprocessing

USERNAME = 'bandit20'
PASSWORD = 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j'

def ssh_client(rank):
    port = 8080
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f'process {rank} connecting...\n')
    client.connect(hostname=utils.ADDRESS, port=utils.PORT, username=USERNAME, password=PASSWORD)

    command = ''
    if rank == 1:
        # first, set up a server that prints out the password to the client
        command = f'echo {PASSWORD} | nc -lp {port}'
    else:
        # execute the client to get the password from the server
        # if the password is correct, then send the password to the server
        command = f'./suconnect {port}'
    
    print(f"process {rank}: {command}\n")
    _, stdout, _ = client.exec_command(command, timeout=5, get_pty=True)
    stdout = stdout.readlines()
    utils.print_stdout(stdout)
    if rank == 1:
        # bandit21 password: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
        print(f"bandit21 password: {utils.get_password(stdout)}")

    client.close()

if __name__ == "__main__":
    # reference: https://www.journaldev.com/15631/python-multiprocessing-example#python-multiprocessing-process-class
    server = multiprocessing.Process(target=ssh_client, args=(1,))
    client = multiprocessing.Process(target=ssh_client, args=(2,))

    # make sure the server is running first
    server.start()
    time.sleep(1)
    client.start()

    server.join()
    client.join()