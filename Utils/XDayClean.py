import os
import sys, time
from stat import *
from os import path
from datetime import datetime, timedelta

ctime = 0
def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''
    global ctime

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        #ctime = datetime.date.fromtimestamp(os.stat(pathname)[ST_CTIME])
        ctime = datetime.fromtimestamp(path.getmtime(pathname))
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print ("Skipping %s" % pathname)

def visitfile(file):
    days_ago = datetime.now() - timedelta(days=5000)
    if ctime < days_ago:
        print ("visiting ", file )# " days_ago ", days_ago)
        #os.remove(file)

if __name__ == '__main__':
    walktree(r"d:\users\vigneshkumarb\downloads", visitfile)
