#!/usr/bin/python3

import tkinter as tk 
import yaml
import db
import time
import os
import view_controler as vc
class Application(tk.Frame):  #定义Application类，派生于Frame类
    def __init__(self,master=None):   #构造函数
        tk.Frame.__init__(self,master)
        self.pack()
        
        self.createWidgets()  #声明对象方法，创建子组件
        
        self.update_all()
        
        
    def createWidgets(self):
        init_min=1
        mfont=('KaiTi',30,'bold')
        self.time_label=tk.Label(self,font=mfont)
        
        self.gold_label=tk.Label(self,font=mfont)
        
    
        self.scale = tk.Scale(self,label="使用时间 （分钟）： ",from_=1, to=120, command=self.pricing)
        self.scale.set(init_min)  # 设置初始值
        
        self.scale.config(width=40,length=300,tickinterval=20,orient=tk.HORIZONTAL)
        
        
        self.cost_label=tk.Label(self,font=mfont,width=30)
        
        # self.time_label=tk.Label(self,font=mfont)
        # self.time_label.pack()
        self.buy_button=tk.Button(self,text='购买',command=self.buy,font=mfont,bg='pink',fg='green',bd=2,width=10,cursor="hand1")
        
        self.pricing(init_min)
        self.exit=tk.Button(self,text='退出',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.logout)
        
        self.wps=tk.Button(self,text='wps',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.wps)
        
        self.music=tk.Button(self,text='网易云音乐',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.music)
        
        self.kidweb=tk.Button(self,text='网络视频学习',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.kidweb)
        
        self.anki=tk.Button(self,text='anki',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.anki)
        # self.anki.pack()
        self.skype=tk.Button(self,text='skype',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.skype)
        self.qq=tk.Button(self,text='qq',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.qq)
        
        self.debug=tk.Button(self,text='测试',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.debug)
        
        self.regold=tk.Button(self,text='刷新',font=mfont,bg='pink',fg='green',bd=2,width=10,command=self.update_gold)
        
        self.daycheck=tk.Button(self,text='签到',font=mfont,bg='pink',fg='green',bd=2,width=10,command=self.daycheck_fun)
        self.mydict=tk.Button(self,text='词典',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.mydict)
        self.cheese=tk.Button(self,text='拍照',font=mfont,bg='pink',fg='green',bd=2,width=10,command=vc.cheese)

        self.time_label.grid(row=0,column=1)
        self.daycheck.grid(row=0,column=2)

        self.gold_label.grid(row=1,column=0)
        self.scale.grid(row=1,column=1)
        self.cost_label.grid(row=1,column=2,columnspan=3)

        self.buy_button.grid(row=2,column=0)
        self.regold.grid(row=2,column=1)
        
        self.exit.grid(row=2,column=2)
        self.debug.grid(row=2,column=3)

        self.wps.grid(row=3,column=0)
        self.music.grid(row=3,column=1)
        #是否打开学习网页
        self.kidweb.grid(row=3,column=2)
        self.skype.grid(row=3,column=3)
        self.mydict.grid(row=3,column=4)
        
        self.cheese.grid(row=4,column=3)
        
    def daycheck_fun(self):
        daychek_code=vc.day_check()
        if(daychek_code==0):
            self.daycheck['text']="已签成功"
        elif(daychek_code==-2):
            self.daycheck['text']="请在12点后签到"
        elif(daychek_code==-3):
            self.daycheck['text']="请在周末签到"
        else:
            self.daycheck['text']="已签到过了"
        self.update_gold()
    def update_gold(self):
        self.time_label['text']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.gold=db.accessGold()
        self.gold_label['text']="剩余金币：{}g".format(self.gold)  
        self.update()  
   
    
    
    def pricing(self,value):
        
        self.sec=int(value)*60
        y=int(value)
        
        self.cost=y
        
        self.cost_label['text']="花费金币：{}".format(y)
    def buy(self):
        if(self.gold<self.cost):
            self.cost_label['text']=("余额不足！")
            return
        v_ret=vc.valid_time(self.sec)
        self.cost_label['text']=v_ret
        if(v_ret!="ok"):
            return
    
    
        

        self.gold-=self.cost
        db.accessGold(self.gold)

        
        db.accessEndTime(self.sec)
       
        self.update_all()
        
        time.sleep(1)
        os.system("/opt/guard/myLogout.py  &")
        exit(0)
       
    def update_all(self):
        self.re_sec=db.accessEndTime()
        self.time_label['text']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.update_gold()
        self.update()
    
    
    
    
    
root=tk.Tk()  #创建一个tk根窗口组件root
root.geometry("1920x1080")
root.config(cursor="arrow ")
app=Application(master=root)  #声明Application对象实例

app.mainloop()  #调用组件mainloop()方法，进入事件循环
