#!/bin/python
# Supplemental
# basic funtion shopping list function
# def in_my_list(item):
#     my_list = ['apples', 'milk', 'butter', 'orange juice']
#     if item in my_list:
#         return ' Basic Got it!'
#     else:
#         return ' Basic Nope!'

# print(in_my_list('apple'))

# print(in_my_list(' chocolate'))

# Using a class to add chocolate with out rewriteing the complete function
class My_list(object):
    my_list = ['apples', 'milk', 'butter', 'orange juice']
    def __init__(self, snack='chocolate'):
        self.snack = snack
    def __str__(self):  # We overwrite the _str_  function from object so that we  print it nice!
        return 'My list: {}'.format(', '.join(self.my_list))
    
    def in_my_list(self,item):
        if item in self.my_list:
            return 'Got it!'
        else:
            return 'Nope!'
    def snack_check(self):
        return self.snack in self.my_list

# december = My_list()

# december.in_my_list('chocolate')
# december.my_list = december.my_list +['chocolate']
# december.in_my_list('chocolate')

# Now we have nice list template for grocery

# jan = My_list()

# december.my_list
# jan.my_list

# This is not helpfull We need to _str_ in class
# print(december)
# print(jan)

# added snack_check function to class and _init_ function
# My favorite snack is chocolate but in Jan  it's apples
# jan = My_list('apples')
# print(jan.snack_check())
# # heck()
# feb = My_list()
# print(feb.snack_check())
# print(dir(object)) #About that object

class caps_list(My_list):
    def in_my_list(self,item):
        response =  super().in_my_list(item)
        return response.upper()

shouty = caps_list()
print(shouty.in_my_list('chocolate'))
# print(dir(caps_list))
help(super)