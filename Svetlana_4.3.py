## Author: Svetlana
## Date: 16/11/2021 
## Task: to print days in month and  run test 

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

## Create function to check year, month
def days_is_month(year, month):
    if year < 1582 or month > 12 or month < 1:
        print("Incorrect input data, check : ", year, month)
        return None
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year) == True and month == 2:
        Days = 29
        #print("Days in month: ", Days, " for Year: ", year, " and Month: ",month)  
    else:
        Days = days[month - 1]
    print("Days in month: ", Days, " for Year: ", year, " and Month: ",month)  
    return Days

###  Enter  year, month  values 
Years_list = [] ### list with input year
results = []    ### list with function results
Year = int(input("Enter Year: "))
Month = int(input("Enter Month: "))
Days = days_is_month(Year, Month)
if Days is None:
    exit()
############################################################################
### CHECK Code
############################################################################
test_years = [1900, 2000, 2016, 1987]
test_month = [2,2,1,11]
test_results = [28, 29, 31, 30]
print("\nTEST DATA")
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_month[i]
    print(yr, "->", end="")
    result = days_is_month(yr,mo)
    if result == test_results[i]:
        print("OK")
    else: 
        print("Failed")    