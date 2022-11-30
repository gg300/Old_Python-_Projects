from tkinter import *
root = Tk()
label = Entry(text="Lololololololololl")
button_1= Button(text="1",padx=10,pady=10)
button_2= Button(text="2",padx=10,pady=10)
button_3= Button(text="3",padx=10,pady=10)
label.grid(row=0,column=2,padx=5,pady=5)
button_1.grid(padx=2,pady=2,row=1,column=1)
button_2.grid(padx=2,pady=2,row=1,column=2)
button_3.grid(padx=2,pady=2,row=1,column=3)


root.mainloop()
