## Author: Svetlana
## Date: 18/11/2021 
## Task: Create function mysplit to split string with blank 

def mysplit(str_input):
    list =[]
    start =0
    str = str_input.strip(" ")
    length = len(str)
    for i in range(length):
    #print(ord(str[i]))
        if (ord(str[i]) == 32):
            list.append(str[start:i])
            start = i + 1
    list.append(str[start:])
    #print("list", list)        
    return(list)

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))