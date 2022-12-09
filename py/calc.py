from tkinter import *
root=Tk()
e=Entry()
global t1
t1=0
global t2
global op

def click0():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(0))
def click1():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(1))
def click2():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(2))
def click3():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(3))
def click4():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(4))
def click5():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(5))
def click6():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(6))
def click7():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(7))
def click8():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(8))
def click9():
    x=0
    for i in e.get():
        x=x+1
    e.insert(x,str(9))

def clickadd():
    global t1
    t1=float(e.get())
    global op 
    op="+"
    e.delete(0,END)
def clicksub():
    global t1
    t1=float(e.get())
    global op 
    op="-"
    e.delete(0,END)
def clickmult():
    global t1
    t1=float(e.get())
    global op 
    op="*"
    e.delete(0,END)
def clickdiv():
    global t1
    t1=float(e.get())
    global op 
    op="/"
    e.delete(0,END)
def clickeq():
    global t2
    t2=float(e.get())
    e.delete(0,END)
    if(op=="+"):
        e.insert(0,str(t1+t2))
    if(op=="-"):
        e.insert(0,str(t1-t2))
    if(op=="*"):
        e.insert(0,str(t1*t2))
    if(op=="/"):
        e.insert(0,str(t1/t2))
def clear():
    e.delete(0,END)
button0=Button(root,text=0,padx=15,pady=10,command=click0)
button1=Button(root,text=1,padx=15,pady=10,command=click1)
button2=Button(root,text=2,padx=15,pady=10,command=click2)
button3=Button(root,text=3,padx=15,pady=10,command=click3)
button4=Button(root,text=4,padx=15,pady=10,command=click4)
button5=Button(root,text=5,padx=15,pady=10,command=click5)
button6=Button(root,text=6,padx=15,pady=10,command=click6)
button7=Button(root,text=7,padx=15,pady=10,command=click7)
button8=Button(root,text=8,padx=15,pady=10,command=click8)
button9=Button(root,text=9,padx=15,pady=10,command=click9)
button_clear = Button(root,text="clear",padx=20,pady=10,command=clear)

button_add=Button(root,text="+",padx=10,pady=10,command=clickadd)
button_sub=Button(root,text="-",padx=10,pady=10,command=clicksub)
button_mult=Button(root,text="*",padx=10,pady=10,command=clickmult)
button_div=Button(root,text="/",padx=10,pady=10,command=clickdiv)
button_eq=Button(root,text="=",padx=10,pady=10,command=clickeq)

e.grid(row=1,column=2)

button0.grid(row=5,column=2)
button1.grid(row=2,column=1)
button2.grid(row=2,column=2)
button3.grid(row=2,column=3)
button4.grid(row=3,column=1)
button5.grid(row=3,column=2)
button6.grid(row=3,column=3)
button7.grid(row=4,column=1)
button8.grid(row=4,column=2)
button9.grid(row=4,column=3)
button_add.grid(row=5,column=1)
button_sub.grid(row=5,column=3)
button_mult.grid(row=6,column=3)
button_div.grid(row=6,column=1)
button_eq.grid(row=6,column=2)
button_clear.grid(row=7,column=2)

root.mainloop()