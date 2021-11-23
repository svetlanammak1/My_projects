list = [6,8,8,4,5,4]
list_temp = []
list.sort()
Len_size = len(list)
print(list, Len_size)
list_temp.append(list[0])
for i in range(Len_size - 1):
    print(i) 
    if list[i] != list[i+1]: 
        list_temp.append(list[i+1])    
print(list_temp)    