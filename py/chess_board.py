def create_chessboard(root,msg:str,kaka,i:int,j:int):
    if (i%2==0)==(kaka%2==0):
        button = Button(root,text=msg,padx=20,pady=20)
    else:
        button = Button(root,text=msg,padx=20,pady=20,bg="gray")
    button.grid(row=i,column=j)
    print(kaka)