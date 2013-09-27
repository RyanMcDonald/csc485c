'''
Created on Sep 27, 2013

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
    document_id = record[0]
    text = record[1]
    
    words = text.split()
    for w in words:
        mr.emit_intermediate(w, document_id) 

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    documents = []
    for v in list_of_values:
        if v not in documents:
            documents.append(v)
        
    mr.emit((key, documents))
    
if __name__ == '__main__':
    # Part 4 
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)