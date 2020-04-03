#!/bin/python

# Multiple line arguments
string2 = """ 
This is 
argument with 
multiple lines"""

print(string2)
test = 'Hello, this is bad world!'
print(test)
print('This test', test.isupper() )

print(test.upper())
test = test.upper()
print('This test', test.isupper() )

print(len(test))



def first_func(x) :
    y = x * 2
    print(y)
    return y

first_func(20)

myfile = open('test.txt', 'r+')

myfile.write('This is a test\n')

test = [line for line in myfile.read()]
print(test)
# for line in myfile.read():
#     print(line)
myfile.close()


mystring = "abc"

example_fstring = f"This is the alphabet starting {mystring}"

print(example_fstring)

#Lambda funtion(no funtion name and single fuction only)
remainder = lambda num, num2: num * num2 
print(remainder(5,2))

# filter function uses lambda fuction
# The Python's filter() function takes a lambda function together with a list as the arguments
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)

# map() function
# The map() function is another built-in function that takes a function object and a list.
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)

# to get help on command 
# help(str)
string3 = 'This is test3' 
print(dir(string3))
