## Author: Svetlana
## Date: 16/11/2021 
## Task: to create is_year_leap function to check leap year,to enter year and check, to run test 

## Create function to check leap year
def is_year_leap(Year):
    if (Year % 400) ==0:
        print("Year: ", Year, " is leap year" )
        return True
    elif (Year % 100) == 0: 
        print("Year: ", Year, " is common year" )  
        return False
    elif (Year % 4) == 0:
        print("Year: ", Year, " is leap year" )
        return True
    else:
        print("Year: ", Year, " is common year" )
        return False


###  Cycle to enter 2 year values, check years and print results
Years_list = [] ### list with input year
results = []    ### list with function results
for i in range(1,3):
    Year = int(input("Enter Year: "))
    if Year < 1582:
        print("Incorrect Year: ", Year, " Year should be more that 1582")
        exit()
    else:
        Years_list.append(Year)
        results.append(is_year_leap(Year))
       #print("Results: ", results)     
print("Years list: ", Years_list)        
print("If Year is leap: ", results)

############################################################################
### CHECK Code
############################################################################
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else: 
        print("Failed")    