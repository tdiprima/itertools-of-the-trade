# Uses itertools.product to generate all pairs of items from a list, excluding
# self-pairs, in a concise manner.

from itertools import product

items = ["x", "y", "z"]

pairs = [(i, j) for i, j in product(items, repeat=2) if i != j]

print(pairs)
