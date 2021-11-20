## Author: Svetlana
## Date: 16/11/2021 
## Task: to get days in year for input Year, Month and Day values 

## Create function to check leap year
def is_year_leap(Year):
    if Year < 1582:
        print("Incorrect input year : ", Year)
        return None    
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
    if  month > 12 or month < 1:
        print("Incorrect input month : ", month)
        return None
    if year == True and month == 2:
        Days = 29
        print("Days in month: ", Days, " for Year: ", year, " and Month: ",month)  
    else:
        Days = days_list[month - 1]
    return Days

## Create function to check year, month. day
def day_of_year(year, month,day):
    Days_Year = 0
    Year_Leap = is_year_leap(year)
    if Year_Leap == None:
        return None
    Days_Month = days_is_month(Year_Leap, month)
    if Days_Month is None:
        return None    
    if day > Days_Month:
        print("Incorrect day was entered: ", day, "for Year: ", year," Month: ", month)
        return None
    if Year_Leap == True:
        Days_Year = sum(days_list_leap[:month-1]) + day
    else:
        Days_Year = sum(days_list[:month-1]) + day           
    return Days_Year      
    

###  Enter  year, month, day  values 
days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
days_list_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
Year = int(input("Enter Year: "))
Month = int(input("Enter Month: "))
Day = int(input("Enter Day: "))
Days = day_of_year(Year, Month,Day)
if Days is None:
    exit()
print("Days in Year: ", Days, " for Year: ", Year, " Month: ", Month, " Day: ", Day)    