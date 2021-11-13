Magic = 3  ## Magic number for compare
Check_cycle = True

while  Check_cycle:
    Number = int(input("Enter number: "))
    if Number == Magic:
        Check_cycle = False
        print("Well down.You are free now")     
    else: print("Ha Ha. You stuck in loop!")