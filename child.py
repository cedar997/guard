#!/usr/bin/python3

import tkinter as tk 
import yaml
import webdb as db
import time
import os
import view_controler as vc
class Application(tk.Frame):  #定义Application类，派生于Frame类
    def __init__(self,master=None):   #构造函数
        tk.Frame.__init__(self,master)
        self.pack()
        
        self.createWidgets()  #声明对象方法，创建子组件
        self.update_all()
        self.update_endtime()
        
    def createWidgets(self):
        mfont=('KaiTi',36,'bold')
        
        self.gold_label=tk.Label(self,font=mfont)
        self.gold_label.pack()
    
        self.scale = tk.Scale(self,label="使用时间 （分钟）： ",from_=0, to=120, command=self.price)
        self.scale.set(20)  # 设置初始值
        self.scale.config(width=40,length=300,tickinterval=20,orient=tk.HORIZONTAL)
        self.scale.pack( )
        
        self.cost_label=tk.Label(self,font=mfont)
        self.cost_label.pack()
        self.time_label=tk.Label(self,font=mfont)
        self.time_label.pack()
        self.buy_button=tk.Button(self,text='购买',command=self.buy,font=mfont,bg='pink',fg='green',bd=2,width=10,cursor="hand1")
        self.buy_button.pack()
        
        self.b2=tk.Button(self,text='退出',font=mfont,bg='pink',fg='green',bd=2,width=10,command=root.destroy)
        self.b2.pack()
        self.checkout=tk.Button(self,text='结账',font=mfont,bg='pink',fg='green',bd=2,width=10,command=self.checkout_fun)
        self.checkout.pack()
    def checkout_fun(self):
        self.gold=db.getGold()
        self.re_sec=db.getEndTime()
        re_gold=self.re_sec//60
        self.gold+=re_gold
        db.setGold(self.gold)
        self.sec=0
        db.setEndTime(0)
        

    def price(self,value):
        
        self.sec=int(value)*60
        y=int(value)
        
        self.cost=y
        
        self.cost_label['text']="花费金币：{}".format(y)
    def buy(self):
        
    
        v_ret=vc.valid_time(self.sec)
        self.cost_label['text']=v_ret
        if(v_ret!="ok"):
            return
        if(self.gold<self.cost):
            self.cost_label['text']=("余额不足！")
            return
        self.gold-=self.cost
        db.setGold(self.gold)
        endTime=db.getEndTime()+self.sec
        
        
       
        db.setEndTime(endTime)
       
        self.update_all()
        
        #os.system("/opt/guard/myLogout.sh "+str(self.sec)+ " &")
       
    def update_all(self):
        self.re_sec=db.getEndTime()
        
        self.update_gold()
        self.update()
    def update_endtime(self):
        self.re_sec-=1
        sec=self.re_sec
        min_=sec//60
        sec_=sec%60
        self.time_label['text']= "剩余时间：{}分{}秒".format(min_,sec_)
        self.after(1000,self.update_endtime)
    def update_gold(self):
        self.gold=db.getGold()
        self.gold_label['text']="剩余金币：{}g".format(self.gold)
    
    def valid_time(self):
        hour=time.localtime().tm_hour
        #min=time.localtime().tm_min
        if(hour<22 and hour >9):
            return True
        return False
root=tk.Tk()  #创建一个tk根窗口组件root
root.geometry("1600x900")
app=Application(master=root)  #声明Application对象实例

app.mainloop()  #调用组件mainloop()方法，进入事件循环
