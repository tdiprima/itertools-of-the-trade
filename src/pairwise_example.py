# Demonstrating the use of itertools.pairwise() to create pairs of 
# consecutive elements from a list.

from itertools import pairwise

print(list(pairwise([10, 20, 30, 40])))
# Output: [(10, 20), (20, 30), (30, 40)]
