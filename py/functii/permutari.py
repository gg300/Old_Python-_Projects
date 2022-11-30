def permutari(string,lol=""):
    if len(string)==0:
        print(lol)
    else:
        for i in range(len(string)):
            letter=string[i]
            front=string[:i]
            back=string[i+1:]
            togh=back+front
            permutari(togh,letter+lol)