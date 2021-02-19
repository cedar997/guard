#!/usr/bin/python3
import requests
host = "http://localhost:8080/"
def getGold():
    
    endpoint = "getGold"

    url = ''.join([host,endpoint])
    r = requests.get(url)
    #response = r.json()
    return int(r.text)
def addGold(gold):
    endpoint = "addGold"
    url = ''.join([host,endpoint])
    data = {"gold":str(gold)}
    res = requests.post(url=url,data=data)
def wifion():  
    endpoint = "wifion"
    url = ''.join([host,endpoint])
    r = requests.get(url)
    
def wifioff():  
    # endpoint = "wifioff"
    # url = ''.join([host,endpoint])
    # r = requests.get(url)
    pass
def setGold(gold):
    endpoint = "setGold"
    url = ''.join([host,endpoint])
    data = {"gold":str(gold)}
    res = requests.post(url=url,data=data)
   

def getEndTime():
    
    endpoint = "getTime"

    url = ''.join([host,endpoint])
    r = requests.get(url)
    #response = r.json()
    r=int(r.text)
    return r
def setEndTime(t):
    
    endpoint = "setTime"
    url = ''.join([host,endpoint])
    data = {"time":str(t)}
    res = requests.post(url=url,data=data)
    print(res.text)
def getday():
    day=-1
    with open("/opt/guard/day","r") as f:
        a=f.read() 
        day=int(a)
    return day
def setday(day):
    with open("/opt/guard/day","w") as f:
        f.write(str(day))
def getState():
    endpoint = "state"
    url = ''.join([host,endpoint])
    r = requests.get(url)
    #response = r.json()
    return int(r.text)
def setState(t):
    endpoint = "state"
    url = ''.join([host,endpoint])
    data = {"state":str(t)}
    res = requests.post(url=url,data=data)
    print(res.text)
if __name__ == '__main__':
    setState(2)