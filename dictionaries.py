#!/bin/python

##Dictionarie
bugs = {"ant": 10, "praying mantis": 0}
print(bugs)
bugs['fly'] = 5 # adding value to dict
print(bugs)
bugs.update({'spider': 1}) # like extend
print(bugs)
# del bugs['spider'] # Removing entry
print(bugs)
print('fly' in bugs)
print(10 in bugs) # can onlu search key not value
print(bugs.get('ant')) # returns none if not found. Does return error!
print(bugs['fly'])

print(bugs.items()) # list of tuples
print(bugs.keys())
print(bugs.values())
print(bugs.get('fly'))
print(bugs.get('spider'))
print(bugs.get('spider', 4))
print(bugs.clear())
print(bugs)
bugs['fly'] = 5
print(bugs)