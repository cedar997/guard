#!/usr/bin/python3
from flask import Flask,request,render_template, Response,redirect, url_for
import db
import os
print("-- guard service stared -")
app = Flask(__name__)
current_state=0
@app.route('/',methods=['GET','POST'])
def hello_world():
    s=db.accessEndTime()
    re_time="0秒"
    gold=db.accessGold()
    if(s>0):
        re_time=str(int(s/60))+"分"+str(s%60)+"秒"
    return render_template('main.html',re_time=re_time,gold=gold)
@app.route('/parent',methods=['GET','POST'])
def parent():
    if request.method=='POST':
        cmd=request.form.get('cmd')
        arg=request.form.get('arg')
        if cmd == 'addgold':
            arg=int(arg)
            db.addGold_(arg)
        elif cmd == "debug":
            arg=int(arg)
            db.accessDebug(1)
        return redirect(url_for('parent'))
    if request.method=="GET":
        s=db.accessEndTime()
        re_time="0秒"
        gold=db.accessGold()
        if(s>0):
            re_time=str(int(s/60))+"分"+str(s%60)+"秒"
        return render_template('parent.html',re_time=re_time,gold=gold)
@app.route('/getGold',methods=['GET'])
def getGoldApi():
    gold=db.accessGold()
    return str(gold)

@app.route('/wifioff',methods=['GET'])
def wifioffApi():
    os.system("sudo nmcli radio wifi off")
    return "wifi off"
@app.route('/wifion',methods=['GET'])
def wifiOnApi():
    os.system("nmcli radio wifi on")
    return "wifi on"
@app.route('/setGold',methods=['POST'])
def setGoldApi():
    if request.method=='POST':
        gold=request.form['gold']
        gold=int(gold)
        db.accessGold(gold)
        return str(gold)
    return "0"
@app.route('/addGold',methods=['POST'])
def addGoldApi():
    if request.method=='POST':
        gold=request.form['gold']
        gold=int(gold)
        db.addGold_(gold)
        return str(gold)
    return "0"
@app.route('/getTime',methods=['GET'])
def getTimeApi():
    t=db.accessEndTime()
    t=int(t)
    return str(t)
@app.route('/setTime',methods=['POST'])
def setTimeApi():
    if request.method=='POST':
        t=request.form['time']
        t=int(t)
        db.accessEndTime(t)
        return str(t)
    return "0"
@app.route('/state',methods=['GET','POST'])
def theStateApi():
    global current_state
    if request.method=='POST':
        t=request.form['state']
        t=int(t)
        current_state=t
        return str(t)
    return str(current_state)
@app.route('/state0',methods=['GET'])
def State0Api():
    global current_state
    if request.method=='GET':
        
        current_state=0
        return "0"
    return str(current_state)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port =8080)
