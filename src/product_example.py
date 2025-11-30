"""
Demonstrating the use of itertools.product() to generate Cartesian products:
It's basically the set of every possible pair you can make by 
matching each element of one set with each element of another.
"""
from itertools import product

# product("AB", repeat=3) is just cranking out every possible 3-letter combo made from A and B, like AAA, AAB, ABA, ... all the way to BBB.
print(list(product("AB", repeat=3)))
# Output: [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'B', 'A'), ('A', 'B', 'B'), ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'B', 'A'), ('B', 'B', 'B')]
