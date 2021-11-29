## Author: Svetlana
## Date: 29/11/2021 
## Task: Create Weeker class with a persistent list of week days. If input week day does not match for day
##       in the list then WeekDayError exception is raised

class WeekDayError(Exception):
    pass


class Weeker:
    list_day = ["Mon", "Tue", "Wen","Thu","Fri","Sat","Sun"]
   
    def __init__(self, day_week):
        self.__day = day_week
        if day_week not in  Weeker.list_day:
            raise WeekDayError 
    
    def __str__(self):
        return(self.__day) 

    def add_days(self, val):
        num_day = -1
        for i in range(len(Weeker.list_day)):
            if Weeker.list_day[i] == self.__day:
                num_day = i
                break

        get_num_day = (num_day + val) % 7
        #print(get_num_day, num_day, val )
        self.__day = Weeker.list_day[get_num_day]

    def subtract_days(self, val):
        num_day = -1
        for i in range(len(Weeker.list_day)):
            if Weeker.list_day[i] == self.__day:
                num_day = i
                break
        if num_day == -1:
            raise WeekDayError      
        get_num_day = (num_day - val) % 7
        #print(get_num_day, num_day, val )
        self.__day = Weeker.list_day[get_num_day]

try:
    weekday = Weeker("Monday")       
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker("Monday")       
    
except WeekDayError:
    print("Sorry, I can't serve your request.")     