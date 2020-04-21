#!/bin/python
#Errors and exception handling

# Example types of errors and how to create them


# for i in range(10)   # Invald syntax error
   
# import builtins      # help(builtins) # too much output, help on all builtins

# 1/0                  # ZeroDivisionError:

# def f():
#     1/0
# f()                  # ZeroDivisionError:

# 1/'0'                # ZeroDivisionError:

# import chris         #  ModuleNotFoundError:

file = open('data', 'w')

# file.read()          # io.UnsupportedOperation:

# Exception Handling
# try and except 

# def f(x):
#     try:
#         print("I am going to convert the input to an integer")
#         print (int(x))
#     except ValueError:
#         print ("Sorry, I was not able to convert that")
# f(2)
# f('2')
# f('two')
# Multiple exceptioons can bee added 
# ... except (TypeError, ValueError)

# Using the as lets us grab exception command

# def be_carefule(a,b):
#     try:
#         print(float(a)/float(b))
#     except (ValueError, TypeError, ZeroDivisionError) as detail:
#         print("Handled Exception", detail)
#     except:
#         print("Unexoected error!")
#     finally:
#         print("THIS WILL ALWAYS RUN!")

# be_carefule(1,0)
# be_carefule(1,[1,2])
# be_carefule(1,'two')
# be_carefule(16**400,1)



# Raising Exceptions

# raise TypeError('You have submitted the wrong type')

class MyPersonalError(Exception):
    pass
# raise MyPersonalError("I am mighty. Hear mr roar!")

def locator (myLocation):
    if (myLocation<0):
        raise MyPersonalError("I am mighty. Hear my roar!")
    print(myLocation)

# locator(-1)

# As Python 3.3 catching exception and raising dfierent one, both execption will be raised

def MyException(Exception):
    pass
try:
    int ("abc")
except ValueError:
    raise MyPersonalError("You can't convert to an integer!")