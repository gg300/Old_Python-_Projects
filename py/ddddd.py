import tkinter as tk
from random import choice
class only_butts:
    def __init__(self,root):
        self.root = root
        root.title()
def start():
    global root 
    global button
    global x,k
    global b 
    b = {}
    k=1
    x=3
    root = tk.Tk()
    root.geometry('320x200+50+50')
    button = tk.Button(text="test",padx=30,pady=10,command=downx)
    label = tk.Label(text=f"{x} ♡",padx=30,pady=10) #lifes
    label.grid(column=0,row=0)
    button.grid(column=0,row=1)
    root.tk.mainloop()
def restart():
    global root
    root.destroy()
    start()
def downx(): #general button function
    global x 
    global b
    inpot = tk.Label(text="Make a guess")
    inpot.grid(row=0,col=1)
    a = [i+1 for i in range(k)]
    checker = choice(a)
    if checker == inpot:
        global k
        for i in range(k):
            key = str(i+1)
            button_gen = tk.Button(text=f"button_{i}",padx=20,pady=20)
            b[key]= button_gen
        k+=1
        pass
    else:
        if x-1>=0:
            x-=1
            label_1 = tk.Label(text=f"{x} ♡",padx=30,pady=10)
            label_1.grid(column=0,row=0)
        else:
            label_lose = tk.Label(text="You lost",padx=10,pady=15)
            label_lose.grid(row=0,column=1)
            button['state'] = 'disabled'
            button_1 = tk.Button(text="start",padx=20,pady=20,command=restart)
            button_1.grid(row=2,column=1)
            button_exit = tk.Button(text="exit",padx=20,pady=20,command=exit)
            button_exit.grid(column=2,row=2)