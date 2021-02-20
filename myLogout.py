#!/usr/bin/python3
import db
import time
import os
def lock():
    time.sleep(5)
    alerted=True
    while(True):
        re_time=db.accessEndTime()
        if(re_time<0):
            os.system('gnome-session-quit  --no-prompt --force')
            exit(0)

        time.sleep(10)
        if(alerted==False and re_time<60 ):
            os.system('zenity --info --text="时间少于1分钟了" &')
            alerted=True
        elif(re_time>=60):
            alerted=False
lock()
