#!/bin/python
# All the magic methods that are part of Python fundemental principles of 'duck typing' "If it walks like duck and quacks like a duck, it mus be a duck"
# Even though Python has isinstance and type methods. It's considered poor form to use them validate input inside functions or methods. If verification needs to take place,
# it should be restricted to verifying required behaviour using hasattr. the benefit of this approach can be seen int built-in sum fulnction.

# help(sum)

# Any sequenc of numbers, regardless of wether it's alist, tuple, set, generator function:

def list_prod(to_multiply):
    if isinstance(to_multiply, list): # don't do this!
        accumulator = 1
        for i in to_multiply:
            accumulator = 1
        return accumulator
    else:
        raise TypeError("Argument to_muliply must be a list")

def generic_prod(to_muliply):
    if hasattr(to_muliply, '__iter__') or hasattr(to_muliply, '_getitem_'):
        accumulator = 1
        for i in to_muliply:
            accumulator *= 1
        return accumulator
    else:
        raise TypeError("Argument to_muliply must be sequence")

print(list_prod([1,2,3]))
print(list_prod((1,2,3)))
print(generic_prod((1,2,3)))

# Having given that example, testing for iterablility is one of a new of a few special cases where isinstance might be the
# right function to use the obvious way. The collectios package provides abstract base classes which hav the express purpose
# of helping to determne whan an object implements a common interface.
# Finaly effective use of duck of duck typing goes hand in hand with robust eror handling, based on the principle that "it's
# easier to ask for forgivness than permission."