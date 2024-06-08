#!/usr/bin/env python
import socket

def find_service_name():
    protocolname = 'tcp'
    #for port in [80, 25]:
    for port in range(80):
        try:
            print(f'Port: {port} => service name: {socket.getservbyport(port,protocolname)}')
        except socket.error as err_msg:
            print(f'Port: {port} => error: {err_msg}')
        
    print(f'Port: 53 => service name: {socket.getservbyport(53,'udp')}')

if __name__ == '__main__':
    find_service_name()
