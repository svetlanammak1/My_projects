for i in range(1,3):
    Year = int(input("Enter Year: "))
    if (Year % 400) ==0:
        print("Year: ", Year, " is leap year" )
        continue
    elif (Year % 100) == 0: 
        print("Year: ", Year, " is common year" )  
        continue
    elif (Year % 4) == 0:
        print("Year: ", Year, " is leap year" )
    else: print("Year: ", Year, " is common year" )      
