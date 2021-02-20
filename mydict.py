#!/usr/bin/python3
from subprocess import run
import tkinter as tk 
import re
import sys
from iSearch.isearch import main
import os
import view_controler as vc
class Application(tk.Frame):  #定义Application类，派生于Frame类
    def __init__(self,master=None):   #构造函数
        tk.Frame.__init__(self,master)
        self.pack()
        
        self.createWidgets()  #声明对象方法，创建子组件
        
        
    def createWidgets(self):
        init_min=1
        mfont=('KaiTi',30,'bold')
        self.text=tk.Text(self,width=20,height=2,font=mfont)
        self.find=tk.Button(self,text='查找',font=mfont,bg='pink',fg='green',bd=2,command=self.find_fun)
        
        self.exit=tk.Button(self,text='退出',font=mfont,bg='pink',fg='green',bd=2,command=vc.myexit)
        
        
    
        
        self.text.grid(row=1,column=2)
        self.find.grid(row=2,column=0)
        
        self.exit.grid(row=4,column=2)
        


   
    def find_fun(self):
        src=self.text.get('0.0','end')
        os.system("xterm -e 's "+src+" ' &")
        
    
    
    
root=tk.Tk()  #创建一个tk根窗口组件root
root.geometry("1920x1080")
root.config(cursor="arrow ")
app=Application(master=root)  #声明Application对象实例

app.mainloop()  #调用组件mainloop()方法，进入事件循环

