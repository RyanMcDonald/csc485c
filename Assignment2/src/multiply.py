'''
Created on Oct 4, 2013

@author: Ryan
'''

import sys
import MapReduce

mr = MapReduce.MapReduce()  

def mapper(record):
    matrix_string = record[0]
    row = record[1] # Row
    column = record[2] # Column
    value = record[3]
    
    # Each key should be the (row, column) entry corresponding to the new matrix product.
    # The list of values contains every cell from a and b that need to be multiplied together then summed.
    if matrix_string == "a":
        for i in range(5):
            mr.emit_intermediate((row, i), (matrix_string, column, value))
    elif matrix_string == "b":
        for i in range(5):
            mr.emit_intermediate((i, column), (matrix_string, row, value))

def reducer(key, list_of_values):
    #print str(key) + " -- " + str(list_of_values)
    
    result = 0
    # The list of values is the rows of A and columns of B for the corresponding cell in the product matrix
    for v1 in list_of_values:
        # Only go through the A values, otherwise we would be doing the calculations twice.
        if v1[0] == "a":
            # Go through the list again, finding the value to multiply the current one with
            for v2 in list_of_values:
                # Ignore other values from the same matrix and check that the row of A matches the column of B
                if v1[0] != v2[0] and v1[1] == v2[1]:
                    result += v1[2] * v2[2]
        
    mr.emit((key[0], key[1], result))
    
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)