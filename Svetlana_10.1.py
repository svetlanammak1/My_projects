## Author: Svetlana
## Date: 01/12/2021 
## Task: The program reads file, counts Latin letters and prints them 
##       the first way: the program uses list to save data 
##       another way uses dictionary in Svetlana_10.2.py 
##       The program uses file.txt to check
from os import strerror

def list_add(ch, num):
    Check_list  = ch in list_ch
    
    if Check_list == False:
        list_ch.append(ch)
        list_num.append(num) 
        return

    for i in range(len(list_ch)):
        if ch == list_ch[i]:
            list_num[i] += num
            break
    
try:
    lcnt = ccnt = 0
    list_ch = []
    list_num = []
    inp_file = input("Enter file name:  ")
    src_file = open(inp_file, 'rt')
    #file.txt
    for line in src_file:
        lcnt +=1
        #counters = {chr(ch): 0 for ch in range(ord('a'), ord('z')+1)} 
        for cc in range(ord('a'), ord('z') + 1):
            ccnt = 0
            for i in range(len(line)):
                if chr(cc) == line[i].lower():
                    ccnt +=1
            if ccnt > 0:        
               list_add(chr(cc), ccnt)
                   
    for i in range(len(list_ch)):
        print(list_ch[i], '->', list_num[i] )  
    src_file.close()    
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))  
    exit(e.errno)

