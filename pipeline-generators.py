#!/bin/python

#Pipeline with Geneerators

from pprint import pprint
import random

def split_float(v):
    '''
    Takes a float or string of a float
    and retuns a tuple containing the
    integer part and the fractional part
    of the number, as string, respectively.
    '''
    v = str(v)
    i, f = v.split('.')
    return (1, '0'+f)

# The Pipeline
# Here we have a pipeline of four generators, each feeding the one below it. WE pprint out the final resulting 
# list after all the stages have complete.
# See the comments sfter each line for further explanation.

rand_gen = ( random.random() * 100 for i in range(200)) #genearat 200 random floats between 0 and 100, one at a time
results = ( split_float(r) for r in rand_gen) # call our split _float() function which will generate the coresponding tuples
results = (r[1] for r in results ) # we only care about the functional part, so only keep of the tuple
results = ( float(r) for r in results) # convert our fractional value from string back into a float

pprint(list(results)) # print the final result

# Why not a for-loop?
# We could have put all the steps of our piple into a sigle for-loop, but we got a couple advantages by breaking stagees out into sepearate
# generators.
# 1. Theres's some calrity gained by having distinct stages specified as a pipeline. people reading code can clearly see the transforms.
# 2. In a for-loop, Python simply computes the values sequentially: there's no chance for automatic optimisation or multi-treading. By breaking
# the tages out, each stage executes in parrallel, just like your washer and dryer.

# Another (Pseudo)-Example

# import json
# results = (json.loads(result) for result in db_cursor.execute(my_query))
# results = ( r['results'] for r in results)
# results = ( [ r['name'], r['type'], r['count'], r['source'] ] for r  in results)

# Filters
# We can even filter our data in pur generator pipeline

# results = ( r for r in results if r[2] > 0 ) # remove reslults with a count of zero
# foo(results) # do something else with your results
