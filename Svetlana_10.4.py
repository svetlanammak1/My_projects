## Author: Svetlana
## Date: 29/11/2021 
## Task: Create Pizza class to make pizza:
##       if pizza not in pizza list  then PizzaError exception is raised
##       if cheese > 100 TooMuchCheeseError exception is raised


from os import strerror


class Pizza():
    list_of_pizza = ['margherita','capricciosa','calzone']
    def __init__(self):
        pass

    def add_pizza(self, pizza):    
        def __init__(self):
            pass
        self.pizza = pizza
        Pizza.list_of_pizza.append(self.pizza)
        print(self.pizza, ": Successfulle added to list of pizza!")
        print("List of pizzas: ", Pizza.list_of_pizza)

    def remove_pizza(self, pizza):    
        self.__pizza_rem = pizza
        Pizza.list_of_pizza.remove(self.__pizza_rem)    
        print(self.__pizza_rem, ": Successfulle removed from list of pizza!")
        print("List of pizzas: ", Pizza.list_of_pizza)

class PizzaError(Exception):
   def __init__(self, pizza='UNKNOWN', message = ''):
      Exception.__init__(self, message)
      self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uncknown', cheese = '>100 G', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

class Order(Pizza):
    def __init__(self): 
        super().__init__()
        self.orders = {}
        self.counter = 1
        self.message = ""
        
        #self.__fo.close()

    def make_pizza(self, pizza ,cheese):
        
        self.pizza = pizza
        self.__cheese = cheese

        if self.pizza not in  Pizza.list_of_pizza: 
            raise PizzaError(self.pizza, "no such pizza in menu") 
        if self.__cheese  >100:
            raise  TooMuchCheeseError(pizza = self.pizza, cheese = self.__cheese, message="too much cheese")
        self.orders[self.counter] = self.pizza
        print(self.counter,self.orders[self.counter], " : Has successfully created!")
        ## write to file 
        try:
            tt= open('pizza_order2.txt', 'w')
            strout = str(self.counter) + " " + self.orders[self.counter] + " : Has successfully created!\n"
            tt.write(strout)
            print("File successfully written!")  
        
            tt.close()
        except IOError as e:
            print("I/O error occured: ", strerror.errno())    
        self.counter += 1

pizzeria = Order()
# Make order
try:
    fo = open('pizza_order.txt', 'w')
    for (pz, ch) in [('calzone', 0),('margherita', 110),('margherita', 40), ('mafia', 20)]:
       try:
            #fo = open('pizza_order.txt', 'w')
            pizzeria.make_pizza(pz, ch)
       except TooMuchCheeseError as tmce:
            print(tmce, ':', tmce.cheese)
       except PizzaError  as  pe:
           print(pe, ':', pe.pizza)  
    fo.close()
except IOError as e:
          print("I/O error occured: ", strerror.errno())    

print()

## Add pizza
##pizza_obj = Pizza(pizza = ['margherita','capricciosa','calzone'])

for pz in ['pepperoni', 'calzone','margherita', 'mafia']:
   try:
      pizzeria.add_pizza(pz)
   except PizzaError  as  pe:
      print(pe, ':', pe.pizza)  
print()

## Remove pizza
for pz in ['margherita', 'mafia']:
   try:
      pizzeria.remove_pizza(pz)
   except PizzaError  as  pe:
      print(pe, ':', pe.pizza)  
print()



   
        
   