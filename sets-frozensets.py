#!/bin/python
#Sets and Frozensets

# Sets are mutable
# numbers = set([1,1,1,1,1,1,2,3,3,3,3,3,2,2,2,2,2]) # Sets only holds UNIQUE numbers 123
# print(numbers)
# letters = set('TheQuickBrownFoxJumpedOverTheLazyDog'.lower())
# print(letters)
# a = {}
# print(type(a))
# more_numbers = {1,2,3,4,5} # set
# print(type(more_numbers))

# print(numbers.add(4))
# print(numbers.add(5))
# print(numbers)
# print(numbers.update([3,4,7]))
# print(numbers)
# numbers.pop() # could be anything
# print(numbers)
# print(numbers.remove(7))
# print(numbers)
# print(numbers.discard(7)) #  no error
# print(numbers)

#Frozensets are not imutable cannot be updated or added
# a = frozenset([1,1,1,1,2,2,2,2,3,3,3,3,3,3])
# print(frozenset(a))

# house_pets = {'dog','cat', 'fish'}
# farm_animals = {'cow', 'sheep', 'pig', 'dog', 'cat'}

# print(house_pets)
# print(farm_animals)
# print(house_pets & farm_animals) # intersection
# print(house_pets | farm_animals) # union
# print(house_pets ^ farm_animals) # sysmetric difference
# print(house_pets - farm_animals) # asymetric difference

# # Using verbose methods to do the same thing, only accept list and tuple 
# farm_animal_list = list(farm_animals) * 2 # doubles original
# print(farm_animal_list)
# print(house_pets.intersection(farm_animal_list)) # shows duplicates intersection
# print(house_pets.union(farm_animal_list))
# print(house_pets.intersection_update(farm_animal_list))
# print(farm_animal_list)

# # Unlike Numbers or strings sets are foten uncomparable
# house_pets = {'dog','cat', 'fish'}
# print(farm_animals > house_pets)
# print(farm_animals < house_pets)

# exercise 1
a = 100
b = set()
c = set()
d = set()
for i in range(1, a + 1):
    x =c.update([i])
    if (i % 5 == 0):
        # print(i)
        b.update([i])
    if (i % 3 == 0):
        # print(i)
        d.update([i])

print(b)
print(d)

print(b.issubset(d))
# sum1 = c /3
#     sum2 = c /3
#     print(sum1)
#     print (sum2)
