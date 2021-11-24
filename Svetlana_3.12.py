
Var1 = float(input("Enter number: "))
Var2 = input("Enter operation: ")
Var3 = float(input("Enter number: "))
Output = 0

if Var2 == "*":
    Output = Var1 * Var3
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)
elif  Var2 == "-":
    Output = Var1 - Var3 
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)
elif  Var2 == "+":
    Output = Var1 + Var3 
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)
elif  Var2 == "/":
    Output = Var1 / Var3   
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)  
elif  Var2 == "%":
    Output = Var1 % Var3   
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)
elif  Var2 == "//":
    Output = Var1 // Var3 
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)
elif  Var2 == "**":
    Output = Var1 ** Var3  
    print("You entered: .",Var1,Var2,Var3, "Results: ", Output)   
else: print("Incorrect operation: ",Var2, " ! Range:[-,+,*,/,//,**]")          
    

