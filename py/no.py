
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
class only_butts:
    def __init__(self,root):
        self.root = root
    def cre_but(self,but:str,x,y):
        butt = Button(self,text=but,padx=20,pady=20)
        butt.grid(x,y)
root = Tk()
for i in range(2):
    for j in range (3):
        butt = only_butts(root)
        butt.cre_but("lolo",i,j)
root.mainloop()