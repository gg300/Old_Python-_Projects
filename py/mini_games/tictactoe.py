import random
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][1],"  |  ",board[1][2],"  |  ",board[1][3],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][1],"  |  ",board[2][2],"  |  ",board[2][3],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[3][1],"  |  ",board[3][2],"  |  ",board[3][3],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
def draw_move(board,free):
    while True:
        x=random.choice(free)
        if x>3:
            if x>6:
                    board[3][x-6] = "X"
                    break
            else:
                    board[2][x-3]= "X"
                    break
        else:
                board[1][x]="X"
                break
def make_list_of_free_fields(board):
    free=[]
    for rows in range(3):
        for coll in range(3):
            if type(board[rows+1][coll+1])==int:
                free.append(board[rows+1][coll+1])
    return free
def enter_move(board):
    try:
        lol=int(input("Enter your move:"))
        if lol<1 or lol>9:
            print("Move must be in board's range")
            enter_move(board)
        if lol>3:
            if lol>6:
                if type(board[3][lol-6])==int:
                    board[3][lol-6] = "O"
                else:
                    print("Space occupied")
                    enter_move(board)
            else:
                if type(board[2][lol-3])==int:
                    board[2][lol-3]= "O"
                else:
                    print("Space occupied")
                    enter_move(board)
        else:
            if type(board[1][lol])==int:
                board[1][lol]="O"
            else:
                print("Space occupied")
                enter_move(board)
    except:
        print("The number must be int")
        enter_move(board)
def victory_for(board, sign):
    # LINIILE
    for rows in board:
        count = 0
        for coll in rows:
            if coll==sign:
                count+=1
            if count==3:
                return True
    # COLOANELE
    count_1=0
    count_2=0
    count_3=0
    for i in range(3):
        if board[i+1][1]==sign:
            count_1+=1
            if count_1==3:
                return True
        if board[i+1][2]==sign:
            count_2+=1
            if count_2==3:
                return True
        if board[i+1][3]==sign:
            count_3+=1
            if count_3==3:
                return True
    # DIAGONALA PRINCIPALA
    count_d=0
    for i in range(3):
        if board[i+1][i+1]==sign:
            count_d+=1
            if count_d==3:
                return True
    #DIAGONALA SECUNDARA
    count_d2=0
    for i in range(1,4):
        for j in range(1,4):
            if i+j==4:
                if board[i][j]==sign:
                    count_d2+=1
            if count_d2==3:
                return True
    return False
board = [[1],[0,1,2,3],[0,4,5,6],[0,7,8,9]]
free = make_list_of_free_fields(board)
draw_move(board,free)
display_board(board)
while True:
    enter_move(board)
    display_board(board)
    if victory_for(board,"O")==True:
        print("You Won")
        break
    free = make_list_of_free_fields(board)
    draw_move(board,free)
    display_board(board)
    if victory_for(board,"X")==True:
        print("You Lost")
        break
    co=False
    for rows in range(1,4):
        for coll in range(1,4):
            if type(board[rows][coll])==int:
                co=True
    if co==False:
        print("Draw")
        break