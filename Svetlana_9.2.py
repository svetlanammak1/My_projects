## Author: Svetlana
## Date: 29/11/2021 
## Task: Create Pizza class to make pizza:
##       if pizza not in pizza list  then PizzaError exception is raised
##       if cheese > 100 TooMuchCheeseError exception is raised


class Pizza():
    def __init__(self, pizza=[]):
        self.__pizza_list = pizza

    def make_pizza_class(self, pz, ch):
        if pz not in  self.__pizza_list: 
            raise PizzaError(pz, "no such pizza in menu") 
        if ch >100:
            raise  TooMuchCheeseError(pizza = pz, cheese = ch, message="too much cheese")
        print("Pizza ready: ", pz, ':', ch) 
    


class PizzaError(Exception):
   def __init__(self, pizza='UNKNOWN', message = ''):
      Exception.__init__(self, message)
      self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uncknown', cheese = '>100 G', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

## process start
pizza_obj = Pizza(pizza = ['margherita','capricciosa','calzone'])

for (pz, ch) in [('calzone', 0),('margherita', 110), ('mafia', 20)]:
   try:
      pizza_obj.make_pizza_class(pz, ch)
   except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese, ':', tmce.pizza)
        
   except PizzaError  as  pe:
        print(pe, ':', pe.pizza) 
