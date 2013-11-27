#!/usr/bin/python

import socket
import re 
import sys
import __main__

def check_server(address, port):
    s = socket.socket()
    print("Attempting to connect to %s on port %s",(address,port))
    try:
        s.connect((address, port))
        print("Connected to %s on port %s on port %s",(address,port))
        return True
    except socket.error,e:
        print("Connected to %s on port %s failed:" (address, port, e))
        return False

if __name__ == __main__:
    from optparse import OptionParser:
    parser = OPtionParser()
    parser.add_option("-a","--address",dest="address",default="localhost",
                      help="ADDRESS for server", metavar="ADDRESS")
    parser.add_option("-p", "--port", dest="address", default=80,
                      help="PORT for Server",metavar="PORT")
    
    (options,args) = parser.parse_args()
    print('options: %s,args: %s'(options,args))
    check = check_server(option.address, options.port)
    print 'check_server returned %s'%check
    sys.exit(not check)
    
    
    
              
        