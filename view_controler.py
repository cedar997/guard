import datetime
import os
import webdb as db
def time_sec_of_day(dt=None):
    if dt is None:
        dt = datetime.datetime.now()
    return dt.hour*3600+dt.minute*60+dt.second

def valid_time(add_sec):
    start_sec=time_sec_of_day()
    end_sec=start_sec+add_sec
    
    limit_dt=datetime.datetime(hour=21,minute=30)
    limit_sec=time_sec_of_day(limit_dt)
    if(end_sec>limit_sec):
        return "超过最晚时间:{}时{}分".format(limit_dt.hour,limit_dt.minute)
    
    limit_dt=datetime.datetime(hour=17,minute=30)
    limit_sec=time_sec_of_day(limit_dt)
    if(start_sec<limit_sec):
        return "还没到晚上时间，要等到:{}时{}分".format(limit_dt.hour,limit_dt.minute)
    
    return "ok"
def wps():
    os.system("firejail --net=none  wps & ")
def music():
        os.system("firejail --ignore=protocol netease-cloud-music --no-sandbox  &")
def anki():
        #os.system(" anki   &")
        pass
def wechat():
        #os.system(" anki   &")
        pass
def debug():
    exit(0)
def kidweb():
        os.system("/usr/local/bin/electron /opt/guard/kidweb  "+ " &")
        db.setState(2)
        os.system("/opt/guard/screentake.py "+ " &")
def logout():
        db.setEndTime(3)
        os.system("/opt/guard/myLogout.py "+ " &")
        exit(1)
def day_check():
    now=datetime.datetime.now()
    
    if(now.hour<12):
        return -2
    
    day_old=db.getday()
    if(now.day==day_old):
        return -1
    
    db.setday(now.day)
    db.addGold(120)
    #print(db.getGold())
    return 0
    
        
if __name__ == '__main__':
    day_check()
