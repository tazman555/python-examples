#!/bin/python

# list Comprehension
# conditional
# d = [[i, i**2, i**3] for i in range(10) if i % 2]
# print(d)

# Nesting
# e = [[i+j for i in 'abcde'] for j in 'xyz']
# print(e)

# Sorting and reordering
fruit = ['Apple', 'Orange', 'Banana', 'Kiwi', 'Watermelon', 'Apricot']
# fruit.remove(['Kivi', 'Watermelon']) # Does not work . Remove only takes single value. Cannot compare list with str
# Sorted funtion
# sort_fruit = sorted(fruit)
# print(sort_fruit)
# print(sort_fruit == fruit) # False

#internal sort
# fruit.sort()
# print(sort_fruit == fruit) # True


# Reverse ordering using reversed function produces iterator which us be coverted back to list.
# r_fruit = list(reversed(fruit))
# print(r_fruit)

# Reverse ordering list using reverse internal method
# fruit.reverse() # This only reverses but does not sort!
# print(fruit)

# print(r_fruit == fruit)

# Using sorted with true flag
# sorted(r_fruit, reverse=True)

#TUPLES
#Tuples Unmutable cannot be changed
a = (1,2, 'first and second')
print(a)
print('lenght a = ', len(a))
# sorted(a) # erorr cannot str and int
print(a.index(2)) # index of 2
print(a.count(2)) # count occurence
b = '1', '2', '3'
print(type(b))
c_raw = '1'
print(c_raw, type(c_raw))
c_tuple = '1',
print(c_tuple, type(c_tuple))
print(c_raw == c_tuple) # Not the same False
d_raw = ('d')
print(c_raw, type(c_raw))
d_tuple = ('d',)
print(d_tuple, type(d_tuple))
print(d_raw == d_tuple) # Not the same False
