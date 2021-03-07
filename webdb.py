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
    #setState(2)
    print(getGold())
    print(getEndTime())
    import sys
    if(len(sys.argv)>1):
        g=int(sys.argv[1])
        addGold(g)
        print(getGold())

