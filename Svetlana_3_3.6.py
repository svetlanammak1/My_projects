###
Numbers  =[]
Dup = []
Input = input("Enter numbers with blank delimiter: ")
Input_split = Input.split(" ")
Len = len(Input_split)
print("Input:",Input_split, "Len Input_split: ", Len)
## Forms list with int
for i in range(Len):
    Numbers.append(int(Input_split[i])) 
print("Numbers: ", Numbers)   

## Sort
Numbers.sort()
print("Numbers after sort: ", Numbers)   

## Select dups
for i in range(Len - 1):
    if Numbers[i] == Numbers[i+1]:
        Dup.append(Numbers[i+1])
print("Duplicates in Number:", Dup)        




