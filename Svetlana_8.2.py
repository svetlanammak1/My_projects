## Author: Svetlana
## Date: 23/11/2021 
## Task: Create Timer class

class Timer:
    def __init__(self, h, m, s):
        self.__hours = h
        self.__min = m
        self.__sec = s

    def __str__(self):                   ## forms output string 
        sec = to_digit(self.__sec)
        min = to_digit(self.__min)
        hour = to_digit(self.__hours)
        output = hour + ":" + min + ":" + sec
        return  output 
        
    def next_second(self):
        sec_add = self.__sec + 1
        min_add = self.__min
        hour_add = self.__hours
        if sec_add >= 60:
           min_add = self.__min + 1
        if min_add >= 60:
           hour_add = self.__hours + 1
        
           
        if  sec_add >= 60:
            self.__sec = 0
        else:
            self.__sec = sec_add

        if  min_add >= 60:
            self.__min = 0
        else:
            self.__min = min_add           

        if  hour_add >= 24:
            self.__hours = 0
        else:
            self.__hours = hour_add    
    
    def prev_second(self):
        sec_min = self.__sec - 1
        min_min = self.__min
        hour_min = self.__hours
        if sec_min < 0:
           min_min = self.__min - 1
        if min_min < 0:
           hour_min = self.__hours - 1
        
           
        if  sec_min < 0:
            self.__sec = 59
        else:
            self.__sec = sec_min

        if  min_min < 0:
            self.__min = 59
        else:
            self.__min = min_min          

        if  hour_min < 0:
            self.__hours = 23
        else:
            self.__hours = hour_min    
        
   
    def get_timer(self):
        sec = to_digit(self.__sec)
        min = to_digit(self.__min)
        hour = to_digit(self.__hours)
        print(hour, min, sec, sep = ":")

def to_digit(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s    
       

timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

## Check Timer 
print("Check Timer")
timer = Timer(23,1,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)







             
