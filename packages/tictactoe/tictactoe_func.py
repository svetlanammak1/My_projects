import random

process = True
board = [[3*i+j+1 for j in range(3)] for i in range(3)]
#print(board)
get_number = [[1,2,3],[3,5,6],[7,8,9]]  ## get number for computer enter
print(board[0][0], board[0][1], board[0][2])
print(board[1][0], board[1][1], board[1][2])
print(board[2][0], board[2][1], board[2][2])

## Function checks if computer ore user won
def victory_for(board, smb):
    for i in range(3):
        if board[i][0] == smb and board[i][1] == smb and board[i][2] == smb:
            print("Check: row: ",i+1, " populated with ", smb)
            return True
        if board[0][i] == smb and board[1][i] == smb and board[2][i] == smb:
            print("Check: column: ",i+1, " populated with ", smb)
            return True    
    if board[0][0] == smb and board[1][1] == smb and board[2][2] == smb:
            print("Check: diagonal left/right populated with ", smb)
            return True 
    if board[2][0] == smb and board[1][1] == smb and board[0][2] == smb:
            print("Check: diagonal right/left populated with ", smb)
            return True         
    return False

## Function create list with free positions
def make_free_fields(board):
    lev = 1
    lev_j = 0
    global list
    list = []
    for j in range(3):
        lev = lev_j  
        for i in range(3):
            lev_j +=i
            if str(board[j][i]) != "X" and str(board[j][i]) !="O":
                list.append(i + lev+1)  
          
    print("Free numbers list: ",list)
    if len(list) > 0:
       return True   
    return False  

## function for computer enter
def computer_move(board):
    Good_enter = False
    if check_computer_move(board,"X") == True:
        return
    if check_computer_move(board,"O") == True:
        return    
    while Good_enter == False:
         #Comp_input = random.randrange(10)
         Comp_input = random.choice(list)
         if Comp_input in list:
             print("Computer entered: ",Comp_input)
             step = int(Comp_input) - 1
             line = step // 3
             stolb = step % 3
             board[line][stolb] = 'X'
             Good_enter = True

      
## function for user enter
def user_move(board):
    Good_enter = False
    if victory_for(board, "O") == False:
       while Good_enter == False:
           User_num = int(input("Enter number: "))
           if User_num not in list:
              print("Incorrect number:", User_num)
              continue 
           
           print("User entered: ",User_num)
           step = int(User_num) - 1
           line = step // 3
           stolb = step % 3
           board[line][stolb] = 'O'
           Good_enter = True



def check_computer_move(board,smb):
    smb_check = ("X","O")
    for i in range(3):
        #print("check_computer_move")
        if str(board[i][0]) == smb and str(board[i][1]) == smb and str(board[i][2]) not in smb_check:
            board[i][2] = "X"
            print("Computer enter: ", get_number[i][2])
            return True
        if str(board[i][0]) == smb and str(board[i][1]) not in smb_check and str(board[i][2]) == smb:
            board[i][1] = "X"
            print("Computer enter: ", get_number[i][1])
            return True    
        if str(board[i][0]) not in smb_check and str(board[i][1]) == smb and str(board[i][2]) == smb:
            board[i][0] = "X" 
            print("Computer enter: ", get_number[i][0])
            return True
        if str(board[0][i]) == smb and str(board[1][i]) == smb and str(board[2][i]) not in smb_check:
            board[2][i] = "X"
            print("Computer enter: ", get_number[2][i])
            return True    
        if str(board[0][i]) == smb and str(board[1][i]) not in smb_check and str(board[2][i]) == smb:
            board[1][i] = "X"
            print("Computer enter: ", get_number[1][i])
            return True
        if str(board[0][i]) not in smb_check and str(board[1][i]) == smb and str(board[2][i]) == smb:
            board[0][i] = "X"
            print("Computer enter: ", get_number[0][i])
            return True    
    if str(board[0][0]) == smb and str(board[1][1]) == smb and str(board[2][2]) not in smb_check:
            board[2][2] = "X"
            print("Computer enter: ", get_number[2][2])
            return True  
    if str(board[0][0]) == smb and str(board[1][1]) not in smb_check and str(board[2][2]) == smb:
            board[1][1] = "X"
            print("Computer enter: ", get_number[1][1])
            return True 
    if str(board[0][0]) not in smb_check and str(board[1][1]) == smb and str(board[2][2]) == smb:
            board[0][0] = "X"
            print("Computer enter: ", get_number[0][0])
            return True    
    
    if str(board[0][2]) == smb and str(board[1][1]) == smb and str(board[2][0]) not in smb_check:
            board[2][0] = "X" 
            print("Computer enter: ", get_number[2][0])
            return True 
    if str(board[0][2]) == smb and str(board[1][1]) not in smb_check and str(board[2][0]) == smb:
            board[1][1] = "X"
            print("Computer enter: ", get_number[1][1])
            return True 
    if str(board[0][2]) not in smb_check and str(board[1][1]) == smb and str(board[2][0]) == smb:
            board[0][2] = "X"
            print("Computer enter: ", get_number[0][2])
            return True    
    return False
    



def display(board):
    print()
    print("+------+------+------+")
    for i in range(3):
        print("|      "*3, "|",sep="")
        for j in range(3):
            ##print("i:j: ",i,j)
            print("|   "+str(board[i][j])+"  ",end="")
        print("|")
        print("|      "*3, "|",sep="")
        print("+------"*3, "+",sep="")
