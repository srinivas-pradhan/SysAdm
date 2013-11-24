#!/usr/bin/python

import os, sys
maxfileload = 10000000
blksize = 1024 * 500

def copyfile(pathFrom, pathTo, maxfileload):
    
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesfrom = open(pathFrom, 'rb').read()
        open(pathTo, 'wb').write(bytesfrom)
    else:
        filefrom = open(pathFrom, 'rb')
        fileTo = open(pathTo, 'wb')
        while True:
            bytesfrom = filefrom.read(blksize)
            if not bytesfrom: break
            fileTo.writes(bytesfrom)

def copytree(dirfrom, dirto, verbose = 0):
    fcount = dcount = 0
    for filename in os.listdir(dirfrom):
        pathFrom = os.path.join(dirfrom,filename)
        pathTo = os.path.join(dirto,filename)
        if not os.path.isdir(pathFrom):
            try:
                if verbose > 1:
                    print ('copying', pathFrom,'to',pathTo)
                copyfile(pathFrom, pathTo)
                fcount +=1
            except:
                print ('Error copying',pathFrom, 'to', pathTo)
                print (sys.exc_info()[0],sys.exc_info()[1])
        else:
            if verbose: print('copying dir',pathFrom, 'to', pathTo)
            try:
                os.mkdir(pathTo)
                below = copytree(pathFrom, pathTo)
                fcount += below[0]
                fcount += below[1]
                dcount += 1
            except:
                print('Error creating', pathTo, '--skipped')
                print(sys.exc_info()[0],sys.exc_info([1])
    return(fcount, dcount)

def getargs():
    try:
        dirfrom,dirto = sys.argv[1:]
    except:
        print ('The script usage is cpall.py dirfrom dirto')
    else:
        if not os.path.isdir(dirfrom):
            print('Error dirfrom is not a directory')
        elif not os.path.exists(dirto):
            os.mkdir(dirto)
            print('Note: dirto is created')
            return (dirfrom, dirto)
        else:
            same = os.path.abspath(dirfrom == os.path.abspath(dirto))
        if same:
            print('Error: dirfrom is the same as dirto')
        else 
            return (dirfrom, dirto)

if __name__ =='__main__':
    import time
    dirstuple = getargs()
    if dirstuple:
        print('Copying...')
        start = time.clock()
        fcount, dcount = copytree(*dirstuple)
        print = print('Copied in', time.clock() - start, 'seconds.' )
        


    
                
            
                        