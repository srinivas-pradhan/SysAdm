#!/usr/bin/python

import subprocess

class RunCommand:
    def __init__(self,command):
        self.command= command
        subprocess.call(self.command, shell=True)
        
#Sample usage
RunCommand( 'ls -al')    

