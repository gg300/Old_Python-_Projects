from tkinter import *
from random import choice
global x0,y0
x0 = 0
y0 = 1
class only_butts:
    def __init__(self,root):
        self.root = root
    def cre_but(self,but:str,x,y):
        self.butt = Button(self,text=but,padx=20,pady=20)
        self.butt.grid(x,y)
def start():
    global root 
    global button
    global x,k
    global b 
    b = {}
    k=1
    x=3
    root = Tk()
    root.geometry('320x200+50+50')
    button = Button(text="test",padx=30,pady=10,command=downx)
    label = Label(text=f"{x} ♡",padx=30,pady=10) #lifes
    label.grid(column=0,row=0)
    button.grid(column=0,row=1)
    root.mainloop()
def restart():
    global root
    root.destroy()
    start()
def downx(): #general button function
    global x 
    global k
    inpot = Label(text="Make a guess")
    inpot.grid(row=0,column=1)
    a = [i+1 for i in range(k)]
    checker = choice(a)
    if checker == inpot:
        global x0,y0
        x0+=1
        only_butts.cre_but(root,"lolo",x0,y0) #x = k->5/r; y = k%5 
        if(x0==5):
            y0+=1
            x0=0
    else:
        if x-1>0:
            x-=1
            label_1 = Label(text=f"{x} ♡",padx=30,pady=10)
            label_1.grid(column=0,row=0)
        else:
            label_1 = Label(text=f"{0} ♡",padx=30,pady=10)
            label_1.grid(column=0,row=0)
            label_lose = Label(text="You lost",padx=10,pady=15)
            label_lose.grid(row=0,column=1)
            button['state'] = 'disabled'
            button_1 = Button(text="start",padx=20,pady=20,command=restart)
            button_1.grid(row=2,column=1)
            button_exit = Button(text="exit",padx=20,pady=20,command=exit)
            button_exit.grid(column=2,row=2)
start()