from tkinter import *
root=Tk()

global i
i=0

def next():
    global i
    i=i+1
    label=Label(root,text=str(i),padx=15,pady=10)
    label.grid(row=4,column=4)

label1=Label(root,text=" ",padx=15,pady=10)
button=Button(root,text="click",padx=15,pady=7,command=next)

label1.grid(row=1,column=2)
button.grid(row=3,column=4)

root.mainloop()