## Author: Svetlana
## Date: 23/11/2021 
## Task: Create CountingStack class based on Stack class to get counter values


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
        
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counting = 0

    def get_counter(self):
        return self.__counting

    def pop(self):
        val = Stack.pop(self)
        self.__counting += 1
        return val        

             
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print("Counter: ", stk.get_counter())    
