## Author: Svetlana
## Date: 23/11/2021 
## Task: Create Queue class to put, get data and QueueError to process exception

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__queue_list = []
        
    def put(self, val):
        self.__queue_list.append(val)
                

    def get(self):
        if len(self.__queue_list) < 1:
            raise IndexError("Queue does not contain element!") 
        val = self.__queue_list[0]
        del self.__queue_list[0]
        return val

             
que = Queue()
que.put("mm")
que.put("dog")
que.put("11")

try:
    for i in range(5):
        print(que.get())
except IndexError as e:  ## added 'as e' to write __str__)
    print("Queue error")
    print(e.__str__())
    

