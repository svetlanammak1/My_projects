
## Apply operations: sort increase, decrease, reverse to input list
################# Step 1:
list_my = []   ## input list
list_rev = []  ## input list to reverse()
list_inc = []  ## input list to sort increase
list_dec = []  ## input list to sort decrease

n = int(input("Enter count: "))
if n < 0:
    print("n<0 : exit") 
    exit()
 
##################    Step 2:
for i in range(n):
    Element = int(input("Enter number: "))
    list_my.append(Element)
print("Step 2(input list: ",list_my)

################# Step 3: sort decreased()
list_dec = list_my.copy() 
swapped = True

while swapped:
    swapped = False
    for i in range(len(list_dec) - 1):
        if list_dec[i] < list_dec[i+1]:
            swapped = True
            list_dec[i] , list_dec[i+1] = list_dec[i+1] , list_dec[i]

print("Step 3 sort decreased: ",list_dec)

################# Step 4: sort increased()
list_inc  = list_my.copy() 
swapped = True

while swapped:
    swapped = False
    for i in range(len(list_inc ) - 1):
        if list_inc [i] > list_inc [i+1]:
            swapped = True
            list_inc [i] , list_inc [i+1] = list_inc [i+1] , list_inc [i]

print("Step 4 sort increased: ",list_inc)

################# Step 5: reverse()
list_rev  = list_my.copy() 
Len = len(list_rev) -1

for i in range(Len):
    if i < Len - i:
        list_rev[i], list_rev[Len - i] = list_rev[Len - i],list_rev[i]
    else:   break    

print("Step 5 list with reverse(): ", list_rev) 

################### Step 6: Standart sort(),reverse()
list_sort = list_my.copy()
list_sort.sort()
print("Step 6: apply standart sort(): ",list_sort)

list_rever = list_my.copy()
list_rever.reverse()
print("Step 6: apply  standart reverse(): ",list_rever)
