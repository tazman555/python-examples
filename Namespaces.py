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
print(locals() == globals()) # local and gloabl are the same as we are at the top level

# Installing Python packages from github
# pip install -e giturl

def altered_cool():
    print(awesome.Awesome('Artisnal vinegar')) # still there?
    # print(coolgroup('the intelligentsia'))
    cool= 'hipster'
    lumberjack = True
    print(sorted(locals().keys()))
    print(locals()['cool'])

altered_cool()

print('lumberjack' in globals())
print(globals()['cool'])

print(globals() == locals())

print(sorted(awesome.__dict__.keys()))

print(dir(awesome) == print(sorted(awesome.__dict__.keys())))

print(awesome.__dict__['cool']) # memory location of cool function

# globals()['coolgroup'] # Not working!!!

print(dir(awe))
print(awe.__dict__['cool'])

print(awe == awesome)

print(id(awe) == id(awesome))

# adding module namesspaces on the fly. Will only last until program exits
def more_awesome():
    return "They're awsome!"
awe.exclaim = more_awesome
print(awe.exclaim())

print('exclaim' in dir(awe))
print('exclaim' in dir(awesome))
print(dir(awe))