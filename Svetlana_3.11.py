### Checked for c0=15
c0  = int(input("Enter number: "))
i1  = 0

while c0 != 1:
    Check_odd = c0 % 2
    i1 += 1
    print(c0,"steps:", i1)
    if Check_odd !=0:
        c0 = 3*c0 + 1
    else:
        c0 = c0/2    