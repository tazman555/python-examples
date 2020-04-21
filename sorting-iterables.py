#!/bin/python
# Sorting using buil in function sorted(x)
# Any thing that is iterable can be sorted
# Pyhton 3, iterable objects must __It_ function explicitly defined

# int_data = [10, 1, 5, 4, 2]
# print("This list has been sorted", sorted(int_data))
# print(int_data)

# int_data.sort()
# print(int_data)

# #To specify how sorting takes place sorted and sort take additional arguments called key.key
# users = ['hAcker1', 'TheBoss', 'botmane', 'turingTest']

# print(sorted(users))
# print(sorted(users, key=str.lower)) # sorted by lower case

# # The __It__ function takes two arguments self and another object normally of the same type.

# class comparableCmp(complex):
#     def __lt__(self, other):
#         return abs(self) < abs(other)

# a = 3+4j
# b = 5+12j

# # a < b
# a1 = comparableCmp(a)
# b1 = comparableCmp(b)

# # a1 < b1

# c = [b1, a1]

# print(sorted(c))

#Another way to do the same comparison is to use the key:

# def magnitude_key(a):
#     return (a*a.conjugate()).real

# magnitude_key(3+4j)

# print(sorted([5+3j, 1j, 35+0j], key=magnitude_key))

# In many cases, we must sort a list dictionaries, lists, or even objects. We could define our own key function
# or several key funtions for different sorting mehods.

list_to_sort = [{'lname':'Jone', 'fname':'Sally'}, {'lname': 'Jones', 'fname':'Jerry'}, {'lname': 'Smith', 'fname': 'John'}, {'lname':'Smiths', 'fname': 'Janice'}]

# print(list_to_sort)

def lname_sorter(list_item):
    return list_item['lname']

def fname_sorter(list_item):
    return list_item['fname']
def lname_then_fname_sorter(list_item):
    return (list_item['lname'], list_item['fname'])

# print(sorted(list_to_sort, key=lname_sorter))
# print(sorted(list_to_sort, key=fname_sorter))
# print(sorted(list_to_sort, key=lname_then_fname_sorter))

# You can use the the standard library operator to perform the sam e task

import operator

lname_sorter = operator.itemgetter('lname') # same as previous example using lname_sorter

# The itemgetter method return a function that is equavalent to the lname_sorter above. Even better, whne passed
# mulitiple arguments, it retruns a tuple containing  thise items in the given order. Moreover, we dont need to give it a name first.
# I is fine to do this.

sorted(list_to_sort, key=operator.itemgetter('lname'))
sorted(list_to_sort, key=operator.itemgetter('lname', 'fname')) # same as using lname_thn_fname_sorter

# To use operator.itemgetter with list s or tuple s, give it a integer indces as arguments. The equivalent function for objects is 
# operator.attrgetter
# Since we know so much about Python now, it's hard to figure out how simple operator.itemgetter actually is: the following finction is essential equivalent:

def itemgetter_clone(*args):
    def f(item):
        return tuple(item[x] for x in args)
        return f
# Obviously operator.itemgetter and intemgetter_clone are not actually simple-it's just that most of the complexity is hidden inside the
# Python internals and arises out tof the fundemental data model
 