import math

class NewValueError(ValueError):
   def __init__(self, name, color , state):
       self.data = (name, color, state)

try:
   raise NewValueError("Enemy warning", "Red alert", "High Readiness")
except NewValueError as nve:
    print(nve.args)    
    for arg in nve.args:
       print(arg, end=' !')
    






class PizzaError(Exception):
   def __init__(self, pizza='UNKNOWN', message = ''):
      Exception.__init__(self, message)
      self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uncknown', cheese = '>100 G', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita','capricciosa','calzone']:
          raise PizzaError  ##(pizza, "no such pizza in menu") 
    if cheese >100:
       raise  TooMuchCheeseError(pizza = pizza, cheese = cheese, message="too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0),('margherita', 110), ('mafia', 20)]:
   try:
      make_pizza(pz, ch)
   except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese, ':', tmce.pizza)
        print(tmce.__str__())

   except PizzaError  as  pe:
        print(pe, ':', pe.pizza) 
