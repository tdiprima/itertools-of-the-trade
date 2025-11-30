# Demonstrating the use of itertools.combinations() and itertools.permutations() for generating combinations and permutations.

from itertools import combinations, permutations

print(list(combinations([1, 2, 3], 2)))
# Output: [(1, 2), (1, 3), (2, 3)]

print(list(permutations([1, 2, 3], 2)))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
