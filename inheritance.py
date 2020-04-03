#!/bin/python
# Inheritance
# The every class inherits the object class fro example the Person inherits from ( sublclass of) the object class
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

class Student(Person):
    bedtime = 'Midnight'
    def do_homework(self):
        import time
        print("I need to work.")
        time.sleep(5)
        print("Did I just fall sleep")
tyler = Student("Tyler", 19)
tyler.species
tyler.talk()
tyler.do_homework()

# To override behavior from the parent class creat a class function with the same name and super function

class Employee(Person):
    def __init__(self, name, age, employer):
        super(Employee, self).__init__(name, age)
        self.employer = employer
    def talk(self):
        talk_str = super(Employee, self).talk()
        return talk_str + " I work for {}".format(self.employer)
fred = Employee("Fred Flintsone", 55, "Slate Rock and Gravel Company")
print(fred.talk())

#python Polymorphism is a class with more than one ancestor, complicated

class StudentEmployee(Student, Employee):
    pass

ann = StudentEmployee("Ann", 58, "Family Services")
print(ann.talk())

# Polymorphism means that different types respond to the same function
# bill = StudentEmployee("bill", 20) # does not work requires employee. As different t