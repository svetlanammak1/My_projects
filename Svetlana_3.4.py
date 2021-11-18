for i in range(1,6):
    Income1 = float(input("Enter income for person: "))
    Tax1 = (Income1/100) * 15 
    print("For person: ",i, "Income: ", Income1,"Round Tax: ", round(Tax1,2))
print("The taxes for 5 persons were processed!")    