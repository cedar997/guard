#!/usr/bin/python3
import sqlite3
import time
dbname="/opt/guard/data/test.db"
def create():
    conn = sqlite3.connect(dbname)
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE user  
        (name           TEXT  PRIMARY KEY     NOT NULL,
       
        gold            INT     NOT NULL,
        time        INT
        );''')
    print ("Table created successfully")
    conn.commit()
    conn.close()
def create_kv():
    conn = sqlite3.connect(dbname)
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE t_kv  
        (key           TEXT  PRIMARY KEY     NOT NULL,
       
        value            TEXT     
        
        );''')
    print ("Table created successfully")
    conn.commit()
    conn.close()
def get(key):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    
    cur.execute("SELECT value FROM t_kv where key= ?",(key,))
    row = cur.fetchall()[0]
    conn.close()
    return row[0]
def init_kv(key,value):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    
    cur.execute("insert into t_kv (key,value) values(?,?);",(key,value))
    conn.commit()
    conn.close()
def set(key,value):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    key=str(key)
    value=str(value)
    cur.execute("update t_kv set value = ? where key = ? ",(value,key))
    conn.commit()
    conn.close()


def accessEndTime(t=None):
    if(t is None):
        end=int(get("time"))
        end=int(end)-int(time.time())
        return end
    else:
        end=t+int(time.time())
        set("time",end)
        return end
def accessGold(gold=None):
    if(gold is None):
        return int(get("gold"))
    else:
        set("gold",gold)
        return gold

def addGold_(x):
    g=accessGold()
    accessGold(g+x)
def accessDay(day=None):
    if(day is None):
        return int(get("day"))
    else:
        set("day",day)
        return day

def accessDebug(debug=None):
    if(debug is None):
        return int(get("debug"))
    else:
        set("debug",debug)
        return debug
if __name__ == '__main__':
    #create_kv()
    #init_kv("time","3")
    #init_kv("day","18")
    #init_kv("debug",0)
    accessDebug(1)
    print(accessDebug())