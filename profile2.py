#!/bin/python
# Profiling is used to determine performance. A profile is a set of statistics that describes how often and for how long various parts of the program executed.
# These statistics can be formatted into reports via the pstats module

import cProfile

def long(upper_limit=100000):
    for x in range(upper_limit):
        pass
def short():
    pass
def outer(upper_limit=100000):
    short()
    short()
    long()

cProfile.run('outer()')
    
cProfile.run('outer(10000000)')

# Easy way run profile on script
# python -m CProfile <myscript>

# Another useful built-in profiler timeit.

# python -m timeit for i in range(100):' ' str(i)'

import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=20000)
mySetup = """
def myfunc(upper_limit=100000):
    return range(upper_limit)
"""

timeit.timeit('myfunc()',number=1000,setup=mySetup)