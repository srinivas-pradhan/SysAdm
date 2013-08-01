#!/usr/local/bin/python3    
import sys
import re
import socket

def check_server(address,port):
    #Create a TCP Socket
    s = socket.socket()
    print ("Attempting to connect %s on port %s") %(address, port)
    try:
        s.connect((address, port))
        print("Connected to %s on port %s") %(address, port)
        return True

    except socket.error:
        print("Connection to %s on port %s failed: %s") % (address, port)
        return False
    
if __name__=="__main__":
    from optparse import OptionParser
    parser = OptionParser()
    
    parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")
    
    parser.add_option("-a", "--port",dest="port", type="int", default=22, help="PORT for Server", metavar="PORT")
    
    (options, args) = parser.parse_args()
    print('options: %s, args: %s') %(options,args)
    check = check_server(options.address,options.port)
    print('check server returned %s') % check
    sys.exit(not check)
    
        