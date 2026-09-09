"""
Method of creating a game

Fundamentally, should support either an key:value pair (JSON adjacency lists),
or a manual user input from a set or arbitrarily large source.

Working off of the example of a default diplomacy game, the two ways [Jacob] invisions this are as follows:

Dynamic growth of adding new items to matrices and lists as they appear. Fuzzy matching to confirm user entry doesn't have errors.
Or, set size creation of blank templates.

Both of these methods need a final pass to alpabetize / order the matrix and list, and also verify the data doesn't have any program defined errors.

"""