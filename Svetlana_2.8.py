x = float(input("Enter number: "))
z = input("Enter operation: ")
y = float(input("Enter number: "))

if z == "+":
    print("Output: ", x+y)
elif z == "-": 
    print("Output: ", x-y)  
elif z == "*": 
    print("Output: ", x*y)  
elif z == "/": 
    print("Output: ", x/y)  
else:
    print("Incorrect operation was entered [+ - * /] ")         