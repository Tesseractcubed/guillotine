"""
Update seems innocent, but is most of the logic of manipulating the files.
I recommend readgame as required reading, and creategame as an end user of changes made here.
"""

def AddNodeAndAdjacencies(node_details): #Adds a node and the adjacencies into the data. Should I allow the node to be added anywhere, or just to the end? Add the node just to the end (less complexity and risk of errors). # Should this be in creategame.py?
    return
def DeleteNodeAndAdjacencies(node_index): # Deletes a node and adjacencies. Permanent operation. # Should this be in deletegame.py?
    return
def MoveNodeAndAdjacencies(node_index,node_index_target): # Allows moving a node and adjacencies to a different index. A pure data transformation, unless some add-ons rely on index based processing (this might cause future bugs).
    return
def UpdateNodeData(node_index,node_schema_index,data): # Looks at data, finds a node, finds the schema index, and returns it. Schema index can be left blank to update all data, or as a list to update several components if data is also a list input.
    data_to_return = 0
    return data_to_return