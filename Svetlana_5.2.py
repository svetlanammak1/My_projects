## Author: Svetlana
## Date: 18/11/2021 
## Task: Fibonacci numbers. Test from -1 - 25  

## Fuction  creates Fibonacci numbers and prints
def  fib(n,start = 1):
    f1 = f2 = 1
    sum=0
    
    for i in range(start, n+1):
        if i < 1:
            print(None ,end=' ')
            continue 
        if i < 3:
            print(1, end=' ')     
            continue
        sum = f1 + f2
        f1, f2 = f2, sum 
        print(f2 ,end=' ')
        
Input_num = int(input("Enter number: "))
fib(Input_num)        

###################################################
################### TEST###########################
print()
fib(25,-1)
