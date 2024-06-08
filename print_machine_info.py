#!/usr/bin/env python
import socket

def print_machine_info():
    machine_name = socket.gethostname()
    machine_address = socket.gethostbyname(machine_name)
    print(f'machine name: {machine_name}')
    print(f'machine address: {machine_address}')


if __name__ == '__main__':
    print_machine_info()
