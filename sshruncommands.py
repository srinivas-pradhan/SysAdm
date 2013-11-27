#!/usr/bin/python

import paramiko

hostname = '10.10.10.12'
port=22
username=''
password=''

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s= paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname,port,username,password)
    stdin,stdout,stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()