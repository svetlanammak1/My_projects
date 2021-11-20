Input = input("Enter 2 numbers with blank delimiter: ")
Input_split = Input.split(" ")
Len = len(Input_split)
print("Input:",Input_split, "Len Input_split: ", Len)
## Forms list with int
Start =int(Input_split[0])
End = int(Input_split[1])
List = []
Count = 0
Sum = 0
if int(Input_split[0]) > int(Input_split[1]):
        Start = int(Input_split[1])
        End = int(Input_split[0])
        print("Warning: input number 2 < input number 1: the process will start from: ", Start)
for k in range(Start,End+1):
    if k % 3 == 0:
        print("Numbers list: ", k)
        List.append(k)
        Count +=1 
        Sum += k
if Count !=0:
    print("List % 3: ",List, "Sum: ", Sum, "Arithsetic Mean: ", Sum/Count )
else:   print("There are no numbers that are divisibled by 3")    