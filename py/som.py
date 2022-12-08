from tkinter import *

root = Tk()
e=Entry(root)
button= Button(root, text="Hey",padx=10,pady=20)
label1= Label(root,text="hi",padx=10,pady=20)

button.grid(row=2, column=1)
e.grid(row=1,column=1)
label1.grid(row=3,column=1)
root.mainloop()