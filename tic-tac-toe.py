grid=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#creating a attractive menu for end-users
def menu():
    print("""
    ++++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++++++++TIK-TAC-TOE++++++++++++++++++++++++
    ++++++++++++++++++GAME++++++++++++++++++++++++++++
          """)
#defined global variable to use in different functions
    global player1
    global player2
    player1=input("Enter your name player1 : ")
    player2=input("Enter your nameplayer2 : ")
#inputs the player's move for x
def input_X():
    row,col=eval(input("{} enter position for x :--row,col").format(player1))
    row,col=row-1,col-1
    if grid[row][col]!=0:
        print("position already filled ")
        print("re",end="")
        input_X()
    else:
        grid[row][col]="X"
#inputs the player's move for O
def input_O():
    row,col=eval(input(f"{player2} enter position for O :--row,col"))
    row,col=row-1,col-1
    if grid[row][col]!=0:
        print("position already filled ")
        print("re",end="")
        input_O()
    else:
        grid[row][col]="O"
def gameboard():
    print(grid[0])
    print(grid[1])
    print(grid[2])
def row_win():
    if grid[0].count("X")==3 or grid[1].count("X")==3 or grid[2].count("X")==3:
        print (f"{player1} wins the game")
        x=1
        print("starting new game")
        tic_tak_toe()
    if grid[0].count("O")==3 or grid[1].count("O")==3 or grid[2].count("O")==3:
        print ("{} wins the game".format(player2))
        x=1
        print("starting new game")
        tic_tak_toe()
def Column_win():
    if grid[0][0]==grid[1][0]:
        if grid[1][0]==grid[2][0]:
            if grid[2][0]=="X":
                print (f"{player1} wins the game")
                x=1
                print("starting new game")
                tic_tak_toe()
            elif grid[2][0]=="O":
                print ("{} wins the game".format(player2))
                x=1
                print("starting new game")
                tic_tak_toe()
    if grid[0][1]==grid[1][1]:
        if grid[1][1]==grid[2][1]:
            if grid[2][1]=="X":
                print (f"{player1} wins the game")
                x=1
                print("starting new game")
                tic_tak_toe()
            elif grid[2][1]=="O":
                print ("{} wins the game".format(player2))
                x=1
                print("starting new game")
                tic_tak_toe()
    if grid[0][2]==grid[1][2]:
        if grid[1][2]==grid[2][2]:
            if grid[2][2]=="X":
                print (f"{player1} wins the game")
                x=1
                print("starting new game")
                tic_tak_toe()
            elif grid[2][2]=="O":
                print ("{} wins the game".format(player2))
                x=1
                print("starting new game")
                tic_tak_toe()
def diagonal_win():
    if grid[0][0]==grid[1][1]:
        if grid[1][1]==grid[2][2]:
            if grid[2][2]=="X":
                print (f"{player1} wins the game")
                x=1
                print("starting new game")
                tic_tak_toe()
            elif grid[2][2]=="O":
                print("{} wins the game".format(player2))
                x=1
                print("starting new game")
                tic_tak_toe()
    if grid[0][2]==grid[1][1]:
        if grid[1][1]==grid[2][0]:
            if grid[2][0]=="X":
                print (f"{player1} wins the game")
                x=1
                print("starting new game")
                tic_tak_toe()
            elif grid[2][2]=="O":
                print("{} wins the game".format(player2))
                x=1
                print("starting new game")
                tic_tak_toe()

def tic_tak_toe():
    menu()
    gameboard()
    x=0
    while x!=1:
        input_X()
        gameboard()
        row_win()
        Column_win()
        diagonal_win()
        input_O()
        gameboard()
        row_win()
        Column_win()
        diagonal_win()
tic_tak_toe()
