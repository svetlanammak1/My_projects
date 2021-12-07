## Author: Svetlana
## Date: 06/12/2021 
## Task: The program runs insert, delete, update, select SQL using todo.d db.


import sqlite3

class NameExc(Exception):
    def __init__(self, head="TODOTaskNameError", message="Bad name"):
            super().__init__(message)
            self.head = head
            self.message = message

class PriorityExc(Exception):
    def __init__(self, head="TODOPriorityError", message="Bad priority"):
            super().__init__(message)
            self.head = head
            self.message = message
class IdExc(Exception):
    def __init__(self, head="TODOIdError", message="Bad ID"):
            super().__init__(message)
            self.head = head
            self.message = message            


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        pass
    
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks
            (id INTEGER PRIMARY KEY ,name TEXT NOT NULL, 
            priority INTEGER NOT NULL)''') 

    def add_task(self):
        name = input("Enter task name: ")
        if len(name) == 0 or name.isspace():
            raise NameExc
        priority = int(input("Enter priority: "))   
        if priority < 1:
            raise PriorityExc

        self.c.execute('INSERT INTO tasks (name, priority) VALUES(?,?)', 
           (name, priority))    
        self.conn.commit()
        #self.conn.close()

    def find_id(self, task_id): 
        self.task_name = task_id
        find = False   
        que =  '''SELECT id, name, priority FROM tasks'''
        rows =  self.c.execute(que)
        for row in rows:
            if row[0] == self.task_name:
               find = True
               return row
        if not find:
            return None      

    
    def update_priority(self):
        priority = int(input("Enter preferable priority: "))
        if priority < 1:
           raise PriorityExc
        numid = int(input("Enter ID: "))   
        if numid < 1:
            raise IdExc
        if self.find_id(numid):
            self.c.execute('''UPDATE tasks SET priority = ? WHERE id = ?''', 
                (priority, numid))    
            self.conn.commit()
        else:
            print('The such id does not exist!')  


    def delete_task(self):
        numid = int(input("Enter id which you want to delete: "))
        if numid < 1:
            raise IdExc
        
        if self.find_id(numid) is not None:
            self.c.execute('''DELETE from tasks  WHERE id = ?''' ,
                (numid,))   
            self.conn.commit()
        else:
            print('The such id does not exist!')          


    
    def show_task(self):
        print("Task table contains the following tasks...")    
        print("ID| Task name | Priority ")
        for row in self.c.execute('''SELECT id, name, priority FROM tasks'''):
            print(row[0], "  ", row[1],
            row[2] )
    def close_conn(self):
        self.conn.close()        

app = Todo()
## menu controller
def menu_controller (put=0):
    print("PUT: ", put)
    if put == 1:
        #show task service
        app.show_task()
    elif put == 2:
        try:
            app.add_task()
        except NameExc as e:
             print(e.message)
        except PriorityExc as e:
             print(e.message)    
        except:
             print("Something goes bady :((")    
        else: print("The task was added successfully!")      
        finally:
            print()
    elif put == 3:
       ## update priority 
        try:
            app.update_priority()
        except NameExc as e:
             print(e.message)
        except PriorityExc as e:
             print(e.message)    
        except:
             print("Something goes bady :((")    
        else: print("The priority was completed successfully!")      
        finally:
            print()        
    elif put == 4:
       ## delete task 
        try:
            app.delete_task()
        except IdExc as e:
             print(e.message)
        except Exception as e:
            print(e.__str__())
            print("Something goes bady :((") 

        else: print("The task was completed successfully!")      
        finally:
            print()        
    
    elif put == 5:
        app.close_conn()
        print("Exit")

        return

    else:
        pass     

while True:
    print('''
     1. Show Tasks
     2. Add Task
     3. Change Priority
     4. Delete task
     5. Exit''' )
    try:
         put = int(input("Put what you want 1 or 2 or 3 or 4 or 5: "))
         if put ==5:
             menu_controller(put)
             break
    except: 
        print("Bad operation")
    else:
        if put in [1,2,3,4]:
            menu_controller(put)            
