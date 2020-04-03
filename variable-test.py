#!/bin/bash
# Libraries to load
import os
import sys
import random

print(dir(os))

z = 'test', 'bed'
print(z)

isinstance(z, str)
print(type([]) is not list) 
print(type(z) is tuple)
isinstance(z, str)

snack1 = " crisps"
snack2 = " cake"
print((snack1 + snack2) * 100)

list1 = ['sugar', 'bread', 'milk', 'butter', 'oil']
print('sugar' in list1)
print(snack2 in list1)
snack1, snack2 = snack2, snack1
print(snack1, snack2)

print(dir(os))
print(os.name)

print(dir(os))

print('\n', dir(random))