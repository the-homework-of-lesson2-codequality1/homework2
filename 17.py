from tkinter import *

count=0
e1=e2=0

def countadd1():
    global count
    count=2

def countadd2():
    global count
    count=1
    
def calculation1():
    root3=Tk()
    frame=Frame(root3)
    global e1,e2,count
    kvar1=e1.get()
    k1=kvar1.isdigit()
    kvar2=e2.get()
    k2=kvar2.isdigit()
    if k1 and k2:
     a=int(e1.get())
     b=int(e2.get())
     s=a*b
     if(count==2):
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

def calculation2():
    root3=Tk()
    frame=Frame(root3)
    global e1,e2,count
    kvar1=e1.get()
    k1=kvar1.isdigit()
    kvar2=e2.get()
    k2=kvar2.isdigit()
    if k1 and k2:
     h=int(e1.get())
     d=int(e2.get())
     s=h*d/2
     if(count==2):
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

def calculation3():
    root3=Tk()
    frame=Frame(root3)
    global e1,e2,count
    kvar1=e1.get()
    k1=kvar1.isdigit()
    if k1:
     r=int(e1.get())
     s=r*r*3.14
     if(count==2):
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
    global e1,e2
    global root2
    root2=Tk()
    root1.quit
    Label(root2,text="长度：").grid(row=0,column=0)
    Label(root2,text="宽度：").grid(row=1,column=0)
    e1=Entry(root2)
    e2=Entry(root2)
    e1.grid(row=0,column=1,padx=10,pady=5)
    e2.grid(row=1,column=1,padx=10,pady=5)
    Button(root2,text="确定",width=10,command=calculation1)\
                                                           .grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root2,text="退出",width=10,command=root2.destroy)\
                                                         .grid(row=3,column=1,sticky=E,padx=10,pady=5)
    root2.mainloop()
    
def triangle():
    root1.destroy()
    global e1,e2
    global root2
    root2=Tk()
    Label(root2,text="高度：").grid(row=0,column=0)
    Label(root2,text="底长：").grid(row=1,column=0)
    e1=Entry(root2)
    e2=Entry(root2)
    e1.grid(row=0,column=1,padx=10,pady=5)
    e2.grid(row=1,column=1,padx=10,pady=5)
    Button(root2,text="确定",width=10,command=calculation2)\
                                                           .grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root2,text="退出",width=10,command=root2.destroy)\
                                                         .grid(row=3,column=1,sticky=E,padx=10,pady=5)
    root2.mainloop()
    
def circle():
    root1.destroy()
    global e1,e2
    global root2
    root2=Tk()
    root1.quit
    Label(root2,text="半径：").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1,padx=10,pady=5)
    Button(root2,text="确定",width=10,command=calculation3)\
                                                           .grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(root2,text="退出",width=10,command=root2.destroy)\
                                                         .grid(row=3,column=1,sticky=E,padx=10,pady=5)
    root2.mainloop()
    
root=Tk()  
def jinru():
    root.destroy()
    global root1
    root1=Tk()
    global count
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
    Radiobutton(root1,text="英寸",variable=v,value=1,command=countadd1).pack(anchor=W)
    Radiobutton(root1,text="厘米",variable=v,value=2,command=countadd2).pack(anchor=W)
    frame1=Frame(root1)
    frame2=Frame(root1)
    frame3=Frame(root1)
    theButton1=Button(frame1,text="方形",command=rectangle)
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



    
