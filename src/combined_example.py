# Demonstrating combining itertools functions like chain, pairwise, and 
# accumulate for composed operations.

from itertools import accumulate, pairwise

data = [5, 10, 20]

print(list(pairwise(accumulate(data))))
# Output: [(5, 15), (15, 35)]
