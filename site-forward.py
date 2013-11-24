#!/usr/bin/python
"""

INCOMPLETE

################################################################################
Create forward-link pages for relocating a web site.
Generates one page for every existing site html file; upload the generated
files to your old web site. See ftplib later in the book for ways to run
uploads in scripts either after or during page file creation.
################################################################################
"""
import os
servername = ''
homedir =''
sitefilesdir =''
uploaddir =''
templatename = ''

try:
    os.mkdir(uploaddir)
except OSError: 

template = open(templatename).read()
sitefiles = os.listdir(sitefilesdir)

count = 0
for filename in sitefiles:
    if filename.emdswith()