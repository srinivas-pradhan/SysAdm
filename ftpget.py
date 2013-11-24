#!/usr/bin/python

import os, sys
from getpass import getpass
from ftplib import FTP

#Defining the user and server params
nonpassive = False
filename = ''
dirname = '.'
site = '' #FQDN host name
userinfo = ('spradh02', getpass ('Pswd?'))

if len(sys.argv) >1 :
    filename = sys.argv[1]
print ('Connecting ...')
connection = FTP(site)
connection.login(userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)
print ('Downloading...')
localfile = open(filename, 'wb')
# connection.retry - Need try and error and error checks for implementation
connection.close()
connection.quit()
localfile.close()

