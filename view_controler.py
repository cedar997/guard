#!/usr/bin/python3
import datetime
import os
import webdb
import db

def time_sec_of_day(hour=None,miniute=0):
    if  hour is None:
        dt = datetime.datetime.now()
        return dt.hour*3600+dt.minute*60+dt.second
    else:
        return hour*3600+miniute*60

def valid_time(add_sec):
    start_sec=time_sec_of_day()
    end_sec=start_sec+add_sec
    h=21
    m=30
    limit_sec=time_sec_of_day(h,m)
    if(end_sec>limit_sec):
        return "超过最晚时间:{}时{}分".format(h,m)
    
    h=17
    m=30
    limit_sec=time_sec_of_day(h,m)
    if(start_sec<limit_sec):
        return "还没到晚上时间，要等到:{}时{}分".format(h,m)
    
    return "ok"
def wps():
    os.system("firejail --net=none  wps & ")
def music():
        os.system("firejail --ignore=protocol netease-cloud-music --no-sandbox  &")
def anki():
        #os.system(" anki   &")
        pass
def skype():
        # os.system("firejail --ignore=protocol skypeforlinux  --no-sandbox  &")
        os.system("firejail skypeforlinux    &")
def debug():
    d=db.accessDebug()
    if(d==1):
        db.accessDebug(0)
        exit(0)
def kidweb():
        os.system("/usr/local/bin/electron /opt/guard/kidweb  "+ " &")
        webdb.setState(2)
        os.system("/opt/guard/screentake.py "+ " &")
def logout():
        db.accessEndTime(3)
        os.system("/opt/guard/myLogout.py "+ " &")
        exit(1)
def day_check():
    now=datetime.datetime.now()
    
    if(now.hour<12):
        return -2
    
    day_old=db.accessDay()
    if(now.day==day_old):
        return -1
    
    db.accessDay(now.day)
    db.accessGold(120)
    
    #print(db.getGold())
    return 0
def myexit():
    exit(0)
def mydict():
    os.system("/opt/guard/mydict.py "+ " &")
if __name__ == '__main__':
    print(valid_time(1*3600))
