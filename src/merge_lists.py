# Demonstrates merging multiple lists into one using itertools.chain
# without creating intermediate structures.

from itertools import chain

list_a = [10, 20]
list_b = [30, 40]
list_c = [50, 60]

merged = list(chain(list_a, list_b, list_c))

print(merged)
