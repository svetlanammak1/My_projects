## Class work examples

from os import strerror


try:
    lcnt = ccnt = 0
    for line in open('file.txt', 'rt'):
        lcnt +=1
        for ch in line:
            print(ch, end='')
            ccnt +=1
        print("\n Characters in file: ", ccnt)    
        print("Lines in file: ", lcnt, "\n")  
      
    
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))          


## Lambda , map functions
list_1 = [x for x in range(5)] 
list_2 = list(map(lambda x: 2 ** x, list_1)) 

print(list_2)   


for x in map(lambda x: x* x, list_2):
    print(x, end =' ')
    print()