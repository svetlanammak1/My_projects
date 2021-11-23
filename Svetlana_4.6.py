## Author: Svetlana
## Date: 16/11/2021 
## Task: to converting liters/km to mile/gallon and  mile/gallon to liters/km

American_mile = 1609.344
American_gallon = 3.785411784

def liters_100km_to_miles_gallon(liters):
    gall = liters/American_gallon
    miles = 100*1000/American_mile
    return  miles/gall   


def miles_gallon_to_liters_100km(miles):
    km = miles * American_mile/1000
    liters = American_gallon * 100
    return liters/km
     
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

