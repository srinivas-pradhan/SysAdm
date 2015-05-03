#!/usr/bin/python

import os
import sys



class linkdirs:
    def __init__(self, fromdir, todir):
        self.fromdir = fromdir
        self.todir = todir
    
    def getfiles_fromdir(self):
        files_to_be_symlinked = []
        for dirpath,dirnames,filenames in os.walk(self.fromdir):
            for fille in filenames:
                fullpath = os.path.join((os.path.join(os.getcwd(), dirpath)), fille)
                files_to_be_symlinked.append(fullpath)
        return files_to_be_symlinked
    
    def makesymlinks(self, symlist):
        for abspath in symlist:
            if self.fromdir == os.path.split(abspath)[0]:
                os.chdir(self.todir)
                os.symlink(os.path.split(abspath)[-1], self.todir)
            else:
                intdir = (os.path.split(abspath)[0]).lstrip(self.fromdir)
                if not os.path.isdir(os.path.join(self.todir, intdir) ):
                    os.mkdir(os.path.join(self.todir, intdir) )
                os.chdir( (os.path.join (self.todir, intdir) ) )
                os.symlink( (os.path.split(abspath)[-1]), self.todir)

if __name__== "__main__":
    if sys.argv != 2 :
        print ("Please do  run the script as lndir.py [fromdir], [todir]")
    copyset = linkdirs()
    fileset = copyset.getfiles_fromdir()
    copyset.makesymlinks(fileset)
    
                
                
                
                
                
        
        

        
        