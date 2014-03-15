#!/usr/bin/python3
import sys
from PP4E.launchmodes import QuietPortableLauncher

numclients = 8
def start(cmdline):
    QuietPortableLauncher(cmdline,cmdline)()

args = ''.join(sys.argv[1:])
for i in range(numclients):
    start('echo-client.py %s' %args)
    