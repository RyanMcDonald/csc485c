'''
Created on Sep 27, 2013

@author: Ryan
'''

import sys
import MapReduce

mr = MapReduce.MapReduce()  

def mapper(record):
    order_id = record[1]
    
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    #joined_records = []
    
    # Get the order item first, to populate the first fields
    order_record = []
    for record in list_of_values:
        if record[0] == 'order':
            order_record = record
            break
    
    # Go through the records again to get the line_items
    for record in list_of_values:
        if record[0] == 'line_item':
            line_item = []
            
            # Copy the order record values over
            for x in range(len(order_record)):
                line_item.append(order_record[x])
                
            # Append the line_item values
            for x in range(len(record)):
                line_item.append(record[x])
                
            #joined_records.append(line_item)
            
            #mr.emit((key, line_item))
            mr.emit(line_item)
        
    #mr.emit((key, joined_records))
    
if __name__ == '__main__':
    # Part 4 
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)