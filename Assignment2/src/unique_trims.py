'''
Created on Oct 4, 2013

@author: Ryan
'''

import sys
import MapReduce

mr = MapReduce.MapReduce()

def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1]
    
    # Trim the last 10 characters off the nucleotides
    nucleotides = nucleotides[:-10]
    
    # Use the resulting nucleotides string as the key because we only want unique values.
    mr.emit_intermediate(nucleotides, sequence_id)
        

def reducer(key, list_of_values):
    mr.emit(key)
    
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)