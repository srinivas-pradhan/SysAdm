#!/usr/bin/python

import paramiko
import os

hostname=''
port=''
username=''
dir_path=''
pkey_file=''

if __name__ == '__main__':
    key= paramiko.RSAKey.from_private_key_file(pkey_file)
    t=paramiko.Transport((hostname,port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files=sftp.listdir(dir_path)
    for f in files:
        print 'Retreiving',f
        sftp.get(os.path.join(dir_path,f),f)
    t.close()
    