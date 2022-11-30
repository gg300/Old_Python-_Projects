
# start()
# def rep(k):
#     for i in range(k):
#         x=int(input("make the guess: "))
#         if(i==x):
#             print("guessed something",sep="-")
#             print(f"now {k+1}")
#             rep(k+1)
#     else:
#         print("Nice try")
# rep(k)

# # 1-> k  - > k=1 .   x = 3 : ) 
# import tkinter as tk
# b = {}
# k=4
# for i in range(k):
#     key = str(i+1)
#     button_gen = tk.Button(text=f"button_{i}",padx=20,pady=20)
#     b[key]= button_gen

# print (b)
from tkinter import *
def prento(kaka):
    print(kaka)

# button['text']  ???????////////////////
 
class loloboton:
    def __init__(self,root,msg:str,kaka,i:int,j:int) -> None:
        self.root = root
        self.kaka = kaka
        self.msg=msg
        self.i=i
        self.j=j
    def lolo_butonu(self):
        button = Button(self.root,text=self.msg,padx=20,pady=20,command=prento(self.kaka))
        button.grid(row=self.i,column=self.j)
        
root = Tk()
koko=0
for i in range(8):
    for j in range (8):
        koko+=1
        hahu = loloboton(root,str(koko),koko,i,j)
        hahu.lolo_butonu()
root.mainloop()
