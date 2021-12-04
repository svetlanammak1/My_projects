## Author: Svetlana
## Date: 01/12/2021 
## Task: The program reads file, splits line , checks format and print dictionary  with names and points 
## class BadLine(StudentsDataException): exception is called:
#        -  if line contains < 3 parts after split
#        - name (part 1 and part2 after split) contains not alphabetical char
#        - part 3 after split contains not number or '.' 
## class BadLine(StudentsDataException): exception is called if file is empty
## The program uses student.txt file to check

from os import strerror
import os

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, line, mes):
        self.__Line = line
        self.__m= mes
        
class FileEmpty(StudentsDataException):
    def __init__(self, name):  
        self.Fname = name      

## function to check input number using allowable values: '.,-,1,2,3,4,5,6,7,8,9'
def Check_Number(input):
    Number_list = ['0','1','2','3','4','5','6','7','8','9']
    count = 0
    
    for i in range(len(input)):
        if input[i] in Number_list:
           continue
        elif input[i] == ".":
             count += 1
        else: 
            return False
    
    if count > 1:  ##or  i <  len(input) -1:
        return  False
    else: return True 

try:
    lcnt = 0
    dict_val = {}
     
    inp_file = input("Enter file name:  ") 
    #inp_file = 'student.txt'
    if os.path.getsize(inp_file):
        pass
        #print("File is not empty")
    else: 
        raise FileEmpty(inp_file) 

    
    src = open(inp_file, 'rt')
    for line in src:
        lcnt +=1
         
        str_file  = line.split()
        len_list = len(str_file)
        ## Exception 
        if len_list < 3:
            raise BadLine(line, ": number parts < 3")  
        ## Exception 
        if str_file[0].isalpha() ==False or str_file[1].isalpha() ==False:
            raise BadLine(str_file, "format string is incorrect")
        ## Exception  check number      
        if Check_Number(str_file[2]) == False:
            raise BadLine(str_file, "format number: " + str(str_file[2]) +" is incorrect") 
        
        key = str_file[0] +" " + str_file[1]
        item = float(str_file[2])
        # Check if key exists in dictionary 
        value = dict_val.get(key)
        if value:
            item += float(value)
        # add to dictionary
        dict_val[key] = item
    print(dict_val)
    for key1 in sorted(dict_val):
        print(key1, dict_val[key1])
    
    src.close()
    
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))  

except  BadLine as e:
    print("Bad format line: ",e.__str__() )   

except FileEmpty as e:
    print("File is empty: ", e.Fname) 


  
