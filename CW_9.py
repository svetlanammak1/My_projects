class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some error")
    else:
        raise ZeroDivisionError("some bad")

for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print("Div by zero")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
         print("My division by zero")
    except ZeroDivisionError:
        print("Original division by zero")