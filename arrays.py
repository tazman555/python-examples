#!/bin/python
a = ['spam', 'eggs', 5, 3.2, [100, 200, 300]]
fruit = ['Apple', 'Orange', 'Pear', 'Lime']
print(a, '\n', fruit)

#Values can be added
fruit.append('Banana')
print(fruit)
fruit.insert(3,'Cherry')
print(fruit)
fruit.append(['kiwi', 'Watermelon'])
print(fruit)
fruit.extend(['Cherry', 'Banana'])
print(fruit)
#removes first insance in the array if multiple matches from the right
fruit.remove('Banana')
print(fruit)

# Removes last entry
fruit.pop()
print(fruit)

# Removes third entry
fruit.pop(3)
print(fruit)

# This works same as extend
newlist= a + fruit
print(newlist)