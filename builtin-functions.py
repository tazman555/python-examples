#!/bin/python
# More Biul-in fuctions

farm_animals = {'horse', 'chicken', 'cow', 'fish'}
generic_container = farm_animals


print(all(generic_container))
print(any(generic_container))

print('horse' in generic_container)
print('horse' not in generic_container)
print(len(generic_container))
print(max(generic_container))
print(min(generic_container))
print(sum([1,2,3,4,5]))