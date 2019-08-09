from tkinter import *
from functools import reduce

system_of_units=0
parm1=parm2=0

def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

def change_sys_to_eng():
    global system_of_units
    system_of_units=2

def change_sys_to_SI():
    global system_of_units
    system_of_units=1
    
def calculation_rec():
    root3=Tk()
    frame=Frame(root3)
    global parm1,parm2,system_of_units
    kvar1=parm1.get()
    kvar2=parm2.get()
    if is_number(kvar1) and is_number(kvar2):
     a=float(kvar1)
     b=float(kvar2)
     s=a*b
     if(system_of_units==2):
      s1=s*6.452
      theLabel=Label(root3,
               text="面积为%.3f平方厘米"%s1,
                compound=CENTER,
                fg="black")
      theLabel.pack()
     else:
      theLabel=Label(root3,
               text="面积为%.3f平方厘米"%s,
               compound=CENTER,
               fg="black")
      theLabel.pack()
    else:
        theLabel=Label(root3,
               text="输入错误，请输入数字",
                compound=CENTER,
                fg="black")
        theLabel.pack()

def calculation_tri():
    root3=Tk()
    frame=Frame(root3)
    global parm1,parm2,system_of_units
    kvar1=parm1.get()
    kvar2=parm2.get()
    if is_number(kvar1) and is_number(kvar2):
     h=float(kvar1)
     d=float(kvar2)
     s=h*d/2
     if(system_of_units==2):
      s1=s*6.452
      theLabel=Label(root3,
               text="面积为%.3f平方厘米"%s1,
                compound=CENTER,
                fg="black")
      theLabel.pack()
     else:
      theLabel=Label(root3,
               text="面积为%.3f平方厘米"%s,
                compound=CENTER,
                fg="black")
      theLabel.pack()
    else:
        theLabel=Label(root3,
               text="输入错误，请输入数字",
                compound=CENTER,
                fg="black")
        theLabel.pack()

def calculation_circle():
    root3=Tk()
    frame=Frame(root3)
    global parm1,parm2,system_of_units
    kvar1=parm1.get()
    if is_number(kvar1):  
     r=float(kvar1)
     s=r*r*3.1415926
     if(system_of_units==2):
      s1=s*6.452
      theLabel=Label(root3,
               text="面积为%.3f平方厘米"%s1,
                compound=CENTER,
                fg="black")
      theLabel.pack()
     else:
      theLabel=Label(root3,
               text="面积为%.3f平方厘米"%s,
                compound=CENTER,
                fg="black")
      theLabel.pack()
    else:
        theLabel=Label(root3,
               text="输入错误，请输入数字",
                compound=CENTER,
                fg="black")
        theLabel.pack()
     
def rectangle():
    root1.destroy()
    global parm1,parm2
    global root2
    root2=Tk()
    root1.quit
    Label(root2,text="长度：").grid(row=0,column=0)
    Label(root2,text="宽度：").grid(row=1,column=0)
    parm1=Entry(root2)
    parm2=Entry(root2)
    parm1.grid(row=0,column=1,padx=10,pady=5)
    parm2.grid(row=1,column=1,padx=10,pady=5)
    Button(root2,text="确定",width=10,command=calculation_rec)\
                                                           .grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root2,text="退出",width=10,command=root2.destroy)\
                                                         .grid(row=3,column=1,sticky=E,padx=10,pady=5)
    root2.mainloop()
    
def triangle():
    root1.destroy()
    global parm1,parm2
    global root2
    root2=Tk()
    Label(root2,text="高度：").grid(row=0,column=0)
    Label(root2,text="底长：").grid(row=1,column=0)
    parm1=Entry(root2)
    parm2=Entry(root2)
    parm1.grid(row=0,column=1,padx=10,pady=5)
    parm2.grid(row=1,column=1,padx=10,pady=5)
    Button(root2,text="确定",width=10,command=calculation_tri)\
                                                           .grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root2,text="退出",width=10,command=root2.destroy)\
                                                         .grid(row=3,column=1,sticky=E,padx=10,pady=5)
    root2.mainloop()
    
def circle():
    root1.destroy()
    global parm1,parm2
    global root2
    root2=Tk()
    root1.quit
    Label(root2,text="半径：").grid(row=0,column=0)
    parm1=Entry(root2)
    parm1.grid(row=0,column=1,padx=10,pady=5)
    Button(root2,text="确定",width=10,command=calculation_circle)\
                                                           .grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root2,text="退出",width=10,command=root2.destroy)\
                                                         .grid(row=3,column=1,sticky=E,padx=10,pady=5)
    root2.mainloop()
    
root=Tk()  
def jinru():
    root.destroy()
    global root1
    root1=Tk()
    global system_of_units
    root.destroy
    global photo
    photo=PhotoImage(file="math.gif")
    theLabel=Label(root1,
                   text="选择单位和图形",
                   image=photo,
                   compound=CENTER,
                   font=("圆幼",40),
                   fg="white")   
    theLabel.pack()
    v=IntVar()
    v.set(2)
    Radiobutton(root1,text="英寸",variable=v,value=1,command=change_sys_to_eng).pack(anchor=W)
    Radiobutton(root1,text="厘米",variable=v,value=2,command=change_sys_to_SI).pack(anchor=W)
    frame1=Frame(root1)
    frame2=Frame(root1)
    frame3=Frame(root1)
    theButton1=Button(frame1,text="矩形",command=rectangle)
    theButton2=Button(frame2,text="三角形",command=triangle)
    theButton3=Button(frame3,text="圆形",command=circle)
    theButton1.pack(fill=X, expand=1)
    theButton2.pack(fill=X, expand=1)
    theButton3.pack(fill=X, expand=1)
    frame1.pack(fill=X, expand=1)
    frame2.pack(fill=X, expand=1)
    frame3.pack(fill=X, expand=1)
    root.mainloop()

    
frame=Frame(root)
global photo
photo=PhotoImage(file="math.gif")
theLabel=Label(root,
               text="面积计算器",
               image=photo,
                compound=CENTER,
                font=("圆幼",50),
                fg="white")
theLabel.pack()
buff=Button(root,text="开始计算",command=jinru)
buff.pack()
root.mainloop()
