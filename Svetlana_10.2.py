## Author: Svetlana
## Date: 01/12/2021 
## Task: The program reads file, counts Latin letters and prints them in count descending order.
##       the program uses stabdard sorted() function with lambda
##       input file : file.txt
##       input empty file : empty.txt
from os import strerror
import os

try:
    ccnt = 0
    dict_val = {}
     
    inp_file = input("Enter file name:  ")
    #  check if file is empty 
    if os.path.getsize(inp_file) > 0:
        ##print("File is not empty")
        pass
    else: 
        print(inp_file,  " file is empty")
        exit()

    file_open = open(inp_file, 'rt')
    str_file  = file_open.read()
    for cc in range(ord('a'), ord('z') + 1):
        ccnt = 0
        for i in range(len(str_file)):
            if chr(cc) == str_file[i].lower():
                    ccnt +=1
                    print(chr(cc), ccnt)
        if ccnt > 0:        
            dict_val[chr(cc)] = ccnt
    print(dict_val)               
    test = dict(sorted(dict_val.items(), key=lambda item: item[1],reverse=True))    
    
    # print results
    for  key in (test):
        print(key,"->", test[key] )
    file_open.close()
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))  

