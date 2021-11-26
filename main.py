## Author: Svetlana
## Date: 23/11/2021 
## Task: Tic-tac-toe game

#import random
#from typing import List
from sys import path
from packages.tictactoe import tictactoe_func

process = True
board = [[3*i+j+1 for j in range(3)] for i in range(3)]


while process == True:
    if tictactoe_func.make_free_fields(board) ==False:
        print("The game ended in a draw")
        break
    tictactoe_func.computer_move(board)
    tictactoe_func.display(board)
    if tictactoe_func.victory_for(board, "X"):
        print("The computer won")
        break    
    if tictactoe_func.make_free_fields(board) ==False:
        print("The game ended in a draw")
        break
    tictactoe_func.user_move(board)
    tictactoe_func.display(board)
    if tictactoe_func.victory_for(board, "O"):
        print("The user won")
        break    

print("End")
 
  

