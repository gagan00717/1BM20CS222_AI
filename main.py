import os
import time
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
         ]
player = 1
win=1
draw=-1
running=0
stop=1

game=running
mark='X'

def DrawBoard():

    print(" %c | %c | %c " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[6], board[7], board[8]))
    print("   |   |   ")

def checkpos(x):
    if(board[x]==' '):
        return  True
    else:
        return False

def gwin():
    global game
    if(board[0]==board[1] and board[1]==board[2] and board[0]!=' '):
        game = win

    elif (board[3] == board[4] and board[4]==board[5] and board[3] != ' '):
        game = win

    elif (board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
        game = win



    elif (board[0] == board[3] and board[3] == board[6] and board[0] != ' '):
        game = win



    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win




    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win


    elif (board[0] == board[4] and board[4] == board[8] and board[4] != ' '):
        game = win
    elif (board[2] == board[4] and board[4] == board[6] and board[4] != ' '):
        game = win

    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[0] != ' '):
        game = draw
    else:
        game = running




print("Tic Tac Toe Game")
print("Player1[X] ________ Player[0]")
print()
print()
time.sleep(3)
while (game == running):
    os.system('cls')
    DrawBoard()
    if (player % 2 != 0):
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if (checkpos(choice-1)):
        board[choice-1] = Mark
        player += 1
        gwin()
        DrawBoard()
os.system('cls')
DrawBoard()
if (game == draw):
    print("Game Draw")
elif (game == win):
    player -= 1
    if (player % 2 != 0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")