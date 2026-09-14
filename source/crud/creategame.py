"""
Method of creating a game

Fundamentally, should support either an key:value pair (JSON adjacency lists),
or a manual user input from a set or arbitrarily large source.

Working off of the example of a default diplomacy game, the two ways [Jacob] invisions this are as follows:

Dynamic growth of adding new items to matrices and lists as they appear. Fuzzy matching to confirm user entry doesn't have errors.
Or, set size creation of blank templates.

Both of these methods need a final pass to alpabetize / order the matrix and list, and also verify the data doesn't have any program defined errors.

"""

# As seen above, we're working on stuffs - lots of them.

def CreateGameFile(): #Creates the boilerplate
    return

def CreateSchema(): #Creates Schema (key value pairs for data lookup and processing)
    return

def CreateBlankGame(node_count,schema): #Creates blank game of a set size with a schema (including the default blank schema)
    return

def CreateGameFromSerialData(serial_data): #Takes serial data (JSON, etc.), deserializes it and calls update functions to apply changes. updategame.py holds the required functions to change and reorder the data.
    return 