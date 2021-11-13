num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
print("Input numbers: ", num1, num2, num3, num4)    
    
if (num1 > num2):
    max = num2
else: max = num1

if (max < num3):
    max = num3

if (max < num4):
    max  = num4
print("Max: ", max)         