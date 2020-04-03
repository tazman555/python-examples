#!/bin/python

#Primitive types
#integer
a, b, c = 24, 24.5, 24j
print(a, b, c)
print(type(a), type(b), type(c))

#string
d, e, f = 'This is my string', r'This raw string ""', u'This is Uencoded'
print(d, e, f)
print(type(d), type(e),type(f))

#bolean 
g, h = True, False
print(g, h)
print(type(g),type(h))


# Input Example 
# Enter items
item1 = input('Enter your first item ')
item2 = input('Enter your second item ')
item3 = input('Enter your third item ')
item4 = input('Enter your fourth item ')
item5 = input('Enter your fifth item ')
total = 9.42 + 5.67 + 3.25 + 13.40 + 7.50
total2 = total * 2
# Display items
print('This is your shopping list')
itemT = [item1, item2, item3, item4, item5]
for x in itemT:
  print(x)

print('Total for 5 items: ', total) 
print('Total for 10 items: ', total2)

string1 = 'blood-oxygeneration level dependent fuctional magnetic resonance imaging'
print('The following string contains:', len(string1), ' characters \n', string1 )

Favsnack = input('Enter your favourite snack ')
Favsnack = Favsnack + ' '
result = (Favsnack * 100)
print(result)

# print(dir(string1))

# help(str.upper)
class GfG : 
    name = "GeeksforGeeks"
    age = 24
  
# initializing object 
obj = GfG() 
  
# use of getattr 
print("The name is " + getattr(obj,'name') + " Age: ", getattr(obj,'age'))
