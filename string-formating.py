#!/bin/python
#String Formating
# String formating is very powerful way to display information to your users.

#empty {} brackets
print('This is a formating String{}'.format("------>hi I'm a formatted String argument<-----"))

print('{2} {1} and {0}'.format('Henry', 'Bill', 'Bob'))

# Arguments can be positional, as illustrated above, or named like the example below

print('{who} is really {what}'.format(who='tony', what='awesome'))

# You can also form lists

cities = ['Dallas', 'Baltimore', 'Dc', ' Austin', 'New York']

print('{0[4]} is really big city'.format(cities))

# Dictionaries as well

lower_to_upper = {'a':'A', 'b':'B', 'c':'C'}

print("This is a big letter {0[a]}".format(lower_to_upper)) # notice no quotes around a

print("This is letter {lookup[a]}".format(lookup=lower_to_upper)) # can be named

for little, big  in lower_to_upper.items():
    print('[-->{0:10} -- {1:10}<-- ]'.format(little, big)) 