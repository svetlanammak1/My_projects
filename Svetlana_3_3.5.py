###
Numbers  =[]
Input = input()
Input_split = Input.split(" ")
Len = len(Input_split)
print("Input:",Input_split, "Len Input_split: ", Len)

for i in range(Len):
    Numbers.append(int(Input_split[i])) 
print("Numbers: ", Numbers, "Sum Numbers:", sum(Numbers))    
