# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    num = int(input("Enter number: "))
 
    lst.append(num) # adding the element
     
print(lst)
## Get max input list
print("MAX value: ",max(lst))
## Get min input list
print("MIN value: ",min(lst))