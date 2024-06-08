#!/usr/bin/env python
import socket

def get_remote_machine_info():
    #remote_host = 'www.python.org'
    remote_host = input('remote host name: ')
    try:
        print(f'IP address of {remote_host}: {socket.gethostbyname(remote_host)}')
    except socket.error as err_msg:
        print(f'{remote_host}: {err_msg}')

if __name__ == '__main__':
    get_remote_machine_info()
