#!/usr/bin/python3
import sqlite3
import time
dbname="/opt/guard/test.db"
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
def get(field):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    name="xzh"
    cur.execute("SELECT "+field+" FROM user where name= ?",(name,))
    row = cur.fetchall()[0]
    conn.close()
    return row[0]
def set(field,value):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    name="xzh"
    cur.execute("update user set "+field+" = ? where name = ? ",(value,name))
    conn.commit()
    conn.close()
def getEndTime():
    end=int(get('time'))
    end=int(end)-int(time.time())
    return end
def setEndTime(t):
    end=t+int(time.time())
    set('time',end)
def getGold():
    return int(get('gold'))
def setGold(gold):
    set('gold',gold)

def addGold(x):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    name="xzh"
    cur.execute("update user set gold= gold + ? where name = ? ",(x,name))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setGold(44)
    print(getGold())
