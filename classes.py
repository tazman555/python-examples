#!/bin/python
# Classes use keyword class
# class Person(object):
#     print("person called")
#     pass

# type(Person)

# print(type(Person) == type(int))  

# nobody = Person()
# print(type(nobody))

# class Person(object):
#     species = " Homo Sapien"
#     def talk(self):
#         return "Hello there, how are you?"


# Example of class with initialisation name. This involves adding name to each instance after class creation a btter way is to _init_ shown below
# nobody = Person()

# print('0', nobody.species)

# print('1', nobody.talk())
# somebody = Person()
# somebody.species= 'Home inernetus'
# somebody.name='Mark'
# print('2', nobody.species)
# Person.species = 'Unknown1'
# print('3', nobody.species)
# print('4', somebody.species)
# Person.name = "Unknown2"
# print('5', nobody.species)
# print('6', somebody.species)
# del somebody.name
# print('7', somebody.name)

# Class using _init_ to initialise class
# class Person(object):
#     species = 'Homo Sapiens'
#     def __init__(self, name='Unknown', age=18): 
#         self.name = name 
#         self.age = age
#     def talk(self):
#         return 'Hello my name is {} age {}'.format(self.name, self.age)


# mark = Person('Mark', age=18)

# generic_voter = Person()
# generic_worker = Person(age=41)
# print(generic_worker.age)
# print(generic_voter.age)
# print(mark.talk())
# print(generic_worker.name) 

# # In Python, it is not unusual to acces attributes directly
# mark.favourite_color =  "green"
# print(generic_worker)
# del generic_worker.name
# # print(generic_worker.name)

# def person_str(self):
#     return "Name: {0}, Age {1}".format(self.name, self.age)

# Person._str_ = person_str

# def person_repr(self):
#     return "Name: {0}, Age {1}".format(self.name, self.age)

# Person._repr_ = person_repr

# print(mark)
# mark

# def person_eq(self, other):
#     return self.age == other.age

# Person._eq_ = person_eq

# bob = Person("Bob", 33)
# bob == mark

class Person(object):
    species = "Home sapiens"
    def __init__(self, name="Unknown", age=18):
        self.name = name
        self.age = age
    def talk(self):
        return "Hello my name is {}.".format(self.name)
    def __str__(self):
        return "Name: {0}, age: {1}".format(self.name, self.age)
    def __repr__(self):
        return "person('{0}', '{1}')".format(self.name, self.age)
    def __eq__(self, other):
        return self.age == other.age

nobody = Person()

bob = Person('Bob', 18)
taz = Person('Taz', 51)
print(nobody.talk())
print(nobody.__str__())
print(nobody.__repr__())
print(nobody.__eq__(bob))