#!/bin/bash
# defining functions

def first_func(x):
    print(x)
    return x * 2
    

# Call function
# first_func(10)
# first_func('Hello')

# no input,output only
def simple():
    pass


def add(a, b):
    return a + b


# print(add(1, 2))

def add2(a, b):
    print(a + b)

# add2(2, 3)

# if loop with elif and else
def even(n):
        if ( type(n) != int):
            print('I only use integers')
        elif ( n % 2 == 0):
            print('I am even number')
        else:
            print('I an odd number')

# even(2)
# even(3)
# even('Hello')



# While loop for ever loop
# while ( 2 + 2 == 4):
#    print('Hello World')

# While that performs task a number times
# i = 0
# while (i <=20):
#     print(i)
#     i += 1

# break to break out of loop
# i = 0
# while (True):
#     i += 1
#     print(i)
#     if ( i == 20):
#         break

# continue to continue insideloop
# i = 0
# while (True):
#     i += 1
#     if ( i == 10):
#         print('I am 10!')
#         continue
#     print(i)
#     if (i == 20):
#         break

#for loop i becomes each value in list
# for i in [1,2,3,4,5,'a','b','c']:
#     print(i, type(i))

# for c in 'orange':
#     print(c)

# for loop fodder: range and xrange
# print(range(10))

#Using range is for loops to count and count backwards
# for i in range(100, 0, -5): # (10) or ( 10, 20) or (0, 100, 5)
#     print(i)

# Using range for index of a loop!
a = 'mystring'
# for i in range(len(a)):
#     print("The character at position " + str(i) + " is " + a[i])

# enumerate is the prefered way to keep track of loop index
# for (i, j) in enumerate(a):
#     print("The character at position " + str(i) + " is " + j)

# for i in range(10000):
#     if (i % 3 == 0):
#         print(i)

