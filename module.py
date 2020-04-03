contents = '''
class Awesome(object):
    def __init__(self, awesome_thing):
        self.thing = awesome_thing
    def __str__(self):
        return "{0.thing} is awesome!!!".format(self)

def cool(group):
    return "Everything is cool when you're part of {0}".format(group)

def main():
    a = Awesome("Everything")
    print(a)

if __name__ == '__main__':
    main()
 #   a = Awesome("Everything")
 #   print(a)
'''

# print(contents)

# def cool():
#     return "Something important is pretty cool"

with open('awesome.py', 'w')  as f:
    f.write(contents)

import importlib
import awesome
importlib.reload(awesome) # This library must have been already been imported

# print(awesome.Awesome("Nobel prize"))
# print(awesome.cool("The A team"))
# print(awesome.a)

# use a nick name for the module
# import awesome as awe

# print(awe.Awesome("A book of Greek aniquities"))
# print(awe.cool("The Python developer community"))
# print(awe.a)

# from awesome import cool

# print(cool("this class"))
# print(Awesome("A peice of Grrek antquestes")) # variable not defined
# print (a) # variable not defined

# from awesome import * # BE CAREFUL

# print(Awesome("A peice of Grrek antquestes")) # variable now defined
# print (a) # variable now defined
# print(cool())

# Name Spaces
print(dir()) # names of itmes in your globalnames space
print(sorted(globals().keys()))
