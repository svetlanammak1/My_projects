## Author: Svetlana
## Date: 19/11/2021 
## Task: to get Factorial

## function to print factorial
def Factor(n,Start = 1):
  if n < 1:
    return None  
  for i in range(Start, n+1):
    if i < 1:
      print(None)
      continue
    elif i < 2:
      out = i
      print(out)
      continue
    else: 
      out *= i
      print(out)  
  return out  

try: 
  Input_number = int(input("Enter number: "))
except:
  print("Incorrect number! Exit")
  exit()
Fact=Factor(Input_number)
print(Input_number,"!: ",Fact)

print("TEST: ")
Fact1 = Factor(9,-1)