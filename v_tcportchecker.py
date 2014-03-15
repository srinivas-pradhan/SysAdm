import optparse
from socket import *
from threading import *
# Code usage [V_tcpportchecker.py -H 19.168.1.1 -p 21,22,8080]

screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect(tgtHost,tgtPort)
        connSkt.send('Violent Python \r\n')
        results = connSkt.recv(1024)
        screenLock.acquire()
        print '[+] %d/ tcp open' %tgtPort
        print '[+]' + str(results)
    except:
        screenLock.acquire()
        print '[-] %d /tcp closed' %tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown Host" %tgtHost
    try:
        tgtName = gethostbyaddr(tgtIp)
        print '\n Scan results for ' + tgtName[0]
    except:
        print '\n Scan results for ' + tgtIp
        setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost,int(tgtPort))) 
        t.start()

def main():
    parser = optparse.OptionParser('usage%prog' +\
                                   '-H <target host>' +\
                                   '-p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', \
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', \
                      help='specify target port[s] separated by comma')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    
    if ( tgtHost == None) | tgtPorts[0] == None ):
        print parser.usage
        exit(0)

if __name__ =="__main__":
    main()           
     
        