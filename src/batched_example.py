# Demonstrating the use of itertools.batched() to group elements into 
# fixed-size chunks.

from itertools import batched

print(list(batched(range(10), 3)))
# Output: [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)]
