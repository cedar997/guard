#!/usr/bin/python3
import webdb
import time
import os
def lock():
    time.sleep(6)
    while(True):
        state=webdb.getState
        if(state==2):
            os.system("scrot  '%Y:%m:%d:%H:%M:%S.png' -e 'mv $f /opt/guard/pic/'")
        if(state==0):
            exit(0)
        time.sleep(120)
        
lock()
