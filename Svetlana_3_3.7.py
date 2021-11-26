###
Numbers  =[]
Input = input("Enter numbers with blank delimiter: ")
Input_split = Input.split(" ")
Len = len(Input_split)
print("Input:",Input_split, "Len Input_split: ", Len)
## Forms list with int
for i in range(Len):
    Numbers.append(int(Input_split[i])) 

Average  = sum(Numbers)/Len
print("Numbers list: ", Numbers, " Average: ", Average)  