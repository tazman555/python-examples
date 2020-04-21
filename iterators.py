#!/bin/python

# List Comprehension
# melist = [ i for i in range(1,100,2)]
# for i in melist:
#     print(i)

# noprimes = [j for i in range(2,19) for j  in range(i*2, 500,i)]
# primes = [x for x in range(2, 500) if x not in noprimes]

# print(sorted(primes))
# #Sorter version. nesting madness
# prime =  [x for x in range(2, 500) if x not in  [j for i in range(2,19) for j  in range(i*2, 500,i)] ]

# print(prime)

#Iterators use __itr__ method and __next__ values fo iterator
# class NonFactorable(object):
#     def __init__(self, *args):
#         self.avoid_multiples = args
#         self.x = 0
#     def __next__(self):
#         self.x += 1
#         while True:
#             if self.x > 200:
#                 raise StopIteration
#             for y in self.avoid_multiples:
#                 if self.x % y ==0:
#                     self.x += 1
#                     break
#             else:
#                 return self.x
#     def __iter__(self):
#            return self
# silent_fizz_buzz = NonFactorable(3,5)
# [x for x in silent_fizz_buzz]
# mostly_prime = NonFactorable(2,3,5,7,13,17,19)
# partial_sum = 0

# for x in mostly_prime:
#     partial_sum +=x
# partial_sum

# mostly_prime = NonFactorable(2 ,3 ,5, 7, 11, 17, 19)
# print(sum(mostly_prime))

# class Square(object):
#     def __init__(self, limit=200):
#         self.limit= limit
#         self.x = 0
    
#     def __next__(self):
#         self.x += 1
#         if self.x > self.limit:
#             raise StopIteration
#         return (self.x-1)**2
    
#     def __getitem__(self, idx):
#         # intitialise counter
#         self.x = 0
#         if not isinstance(idx, int):
#             raise Exception("Only integer index arguments are accepte!d")
#         while self.x < idx:
#             self.__next__()
#         return self.x**2
    
#     def _iter__(self):
#         return self

# my_squares = Square(limit=20)
# [x for x in my_squares]

# print(my_squares[2.5]) #  Only integer index arguments are accepte!d # error
# print(my_squares[5]
# my_squares[25] # we have set limit to 20, we cannot access index location above 20

# Generators
# Generators are iterators with much lighter syntax. very simple look just like comprehension lists accept they surrounded by parentheses () instead of []
# generators use yield instead of return keyword. A generator maintains state in between times when it is called; execution resumes start immediately after the yield statement and continues until the next yield is encountered.

# y = (x*x for x in range(30)
# print(y) # hmm.... not working

# def xsquared():
#     for i in range(30):
#         yield i*i

# def squared_inf():
#     x =0 
#     while True:
#         yield x*x
#         x += 1
# squares = [ x for x in xsquared()]
# print(squares)

# Another example ...days of the week
# def day_of_week():
#     i = 0
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     while True:
#         yield days[i%7]
#         i += 1

# day_of_week()

# import random
# def snowday(prob=.01):
#     r = random.random()
#     if r < prob:
#         return "snowday!"
#     else:
#         return "regular day"
# n = 0
# for x in day_of_week():
#     today = snowday()
#     print(x + " is a " + today)
#     n += 1
#     if today == "snowday!":
#         break

# weekday = (day for day in day_of_week())

# next(weekday)

# pipelining
# One powerful use of generators is to connect them together into a pipeline, where each generator is used by the next.
# Without generators long-running task would become a bottle neck, geenerators allow other steps to continue.

import random


#Get the fraction part of a string rperesntation of a float

def frac_part(v):
    v = str(v)
    i, f = v.split('.')
    return f

# TRADITIONAL APPROACH

results = []
for i in range(20):
    r = random.random() *100        # generate a random numner
    r_str = str(r)                  # convert it to a string
    r_frac = frac_part(r_str)       # get the fractional part
    r_out = float('0.' + r_frac)    # convert it back to float
    results. append(r_out)
results

# generator pipeline
rand_gen = ( random.random() for i in range (20) )
str_gen = ( str(r) for r in rand_gen )
frac_gen = ( frac_part(r) for r in str_gen )
out_gen = ( float('0.' + r) for r in frac_gen)

results = list(out_gen)
print(results)
