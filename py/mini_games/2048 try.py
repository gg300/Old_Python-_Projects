import random
x=(1,2,3,4)
y=(2,4)
board=[[0 for i in range(1,5)] for x in range(1,5)]
def inputt():
        x=input()
        if x == 'a':
            print(" ")
            for rows in board:
                print(rows)
        if x == 'd':
            print(" ")
            for rows in board:
                print(rows)
        if x == 'w':
            print(" ")
            for rows in board:
                print(rows)
        if x == 's':
            print(" ")
            for rows in board:
                print(rows)
def start():
    for i in range(2):
        w=random.choice(x)-1
        c=random.choice(x)-1
        while w==c:
            w=random.choice(x)-1
            c=random.choice(x)-1
        board[w][c]=2
def random_poz():
    w=random.choice(x)-1
    c=random.choice(x)-1
    while w==c and board[w][c]!=0:
        w=random.choice(x)-1
        c=random.choice(x)-1
    v=random.choice(y)
    board[w][c]=v

## test initial
for rows in board:
    print(rows)

## test start
start()
print(" ")
for rows in board:
    print(rows)

# if x==0:
#     x
# if x == y:
#     x+y
for i in range (4):
    for j in range(4,0,-1):
        board[i][j]
    print(board[0][i-1])


    

while True:
    break
    inputt()
    random_poz()