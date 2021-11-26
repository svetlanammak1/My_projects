import platform
from tkinter import *
from tkinter import messagebox 

def clicked1():
    a=platform.platform()  
    messagebox.showinfo("Система", a) 

def clicked2():
    a=platform.machine()
    messagebox.showinfo("Machine", a) 


def clicked3():
    a=platform.processor()
    messagebox.showinfo("Processor", a)     

def clicked4():
    Vers = ""
    a=""
    for atr in  platform.python_version_tuple(): 
        Vers  += atr
    print(Vers)    
    a=platform.python_implementation() + " " + Vers
    print(a)
    messagebox.showinfo("Python", a)         


  
window = Tk()  
window.title("Wekcome ")  
window.geometry('400x300')  
menu = Menu(window)  
new_item = Menu(menu)  
new_item.add_command(label='Processor',command=clicked3)  
new_item.add_separator()  
new_item.add_command(label='System',command=clicked1)  
new_item.add_separator()  
new_item.add_command(label='Machine',command=clicked2)  
new_item.add_separator()  
new_item.add_command(label='Python',command=clicked4) 

menu.add_cascade(label='Select needed info by click', menu=new_item)  
window.config(menu=menu)  
window.mainloop()