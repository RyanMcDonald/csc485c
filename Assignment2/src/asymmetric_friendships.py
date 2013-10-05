'''
Created on Oct 3, 2013

@author: Ryan
'''

import sys
import MapReduce

mr = MapReduce.MapReduce()
 
def mapper(record):
    person = record[0]
    friend = record[1]
    
    # If a person is friends with someone, emit a 1. Emit for the reverse as well, so that way if that person is also friends
    # with this person, then two ones will have been emitted.
    mr.emit_intermediate((person, friend), 1)
    mr.emit_intermediate((friend, person), 1)

def reducer(key, list_of_values):
    if len(list_of_values) < 2:
        mr.emit(key)
    
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)