'''
Created on October 3, 2013

@author: Ryan
'''

import sys
import MapReduce

# Part 1 
mr = MapReduce.MapReduce()  
 
# Part 2 
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    friend = record[1]
    
    mr.emit_intermediate(key, friend) 

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total_friends = {}
    for v in list_of_values:
        if key not in total_friends:
            total_friends[key] = 1
        else:
            total_friends[key] += 1
            
    mr.emit((key, total_friends[key]))
    
if __name__ == '__main__':
    # Part 4 
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)