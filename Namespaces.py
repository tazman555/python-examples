#!/bin/python
# Name Spaces
import awesome
from  awesome import cool

#Global Namespace
# print(dir()) # names of itmes in your globalnames space
# Another way of displaying global namespace
# print(sorted(globals().keys()))
# print(dir() == sorted(globals().keys())) # equal true

# print(globals()['awesome'])
# print(globals()['cool'])
# print(globals()['coolgroup'])

# local Namespace
print(locals())
print(locals() == globals())