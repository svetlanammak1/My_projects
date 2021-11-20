## Author: Svetlana
## Date: 16/11/2021 
## Task: simple calculator with operations: '+,-,/,*,//,%'

Operation_list = ['+','-','/','*','//','**','%']
Number_list = ['0','1','2','3','4','5','6','7','8','9']

def function_exp(num1, num2):
    print("exp: ", num1,"**",num2,"=", num1 ** num2 )
    
def function_minus(num1,num2):
   print("minus: ",num1,"-",num2,"=", num1 - num2 )  

def function_mult(num1,num2):
    print("Mult: ",num1,"*",num2,"=", num1 * num2 )

def function_plus(num1,num2):
    print("plus: ",num1,"+",num2,"=", num1 + num2 )

def function_div(num1,num2):
    if num2 == 0:
        print("division by zero error")
        return None
    print("division: ",num1," / ",num2," = ", num1/num2 )

def function_floordiv(num1,num2):
    print("floor division: ",num1,"//",num2,"=", num1//num2 ) 

def function_mod(num1,num2):
    print("mod:",num1, "%",num2,"=", num1 % num2 )       

## function to check input number using allowable values: '.,-,1,2,3,4,5,6,7,8,9'
def Check_Input(input):
    count = 0
    pos = 0
    for i in range(len(input)):
        if input[i] in Number_list:
           continue
        elif input[i] == ".":
             count += 1
        elif input[i] == "-":
            pos = i
            if i != 0:
                 break      
        else: break
    ##print("pos: ",pos, "i: ",i, "count: ",count,len(input) -1 )    
    if count > 1 or pos !=0 or i <  len(input) -1:
        return  False
    

Num1 = input("Enter number: ")
if Check_Input(Num1) == False:
    print("Incorrect input number: ", Num1)  
    exit()
    
if Num1.isdigit() == True:
    Num1 = int(Num1)
else: Num1 = float(Num1)    

Operation = input("Enter operation: ") 
if Operation not in Operation_list:
    print("You entered incorrect operation: ", Operation)       
    exit()
Num2 = input("Enter number: ")    
if Check_Input(Num2) == False:
    print("Incorrect input number: ", Num2)  
    exit()

if Num2.isdigit() == True:
    Num2 = int(Num2)
else: Num2 = float(Num2)  
    
if Operation == "+":
    function_plus(Num1,Num2)
elif    Operation == "-":
    function_minus(Num1,Num2)
elif    Operation == "*":
    function_mult(Num1,Num2)
elif    Operation == "/":
    function_div(Num1,Num2)    
elif    Operation == "//":
    function_floordiv(Num1,Num2)    
elif    Operation == "%":
    function_mod(Num1,Num2)    
elif    Operation == "**":
    function_exp(Num1,Num2)       
    


       