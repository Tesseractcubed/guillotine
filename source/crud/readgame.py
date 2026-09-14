"""
This is how we get data...

Do I want to implement a version of tensorflow's slicing custom here???
I don't know yet.

Reading needs to access a node or adjacency, and the values that affect it.
Reading also needs to be able to slice data to view a subset of all data in the matrix or list.

Fundamentally, updating data relies on logic from reading data, or at least location information.
"""
def ReadNodeData(node_index,node_schema_index): # Returns data present for the node at a schema index. Schema can be left blank to return all node data.
    return

def ReadAdjacencyData(array_row_index,array_column_index,adjacency_schema_index): # Returns data present for the adjacency at a schema index. Schema can be left blank to return all adjacency data.
    return