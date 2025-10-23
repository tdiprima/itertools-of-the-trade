"""
Generates all pairs of items from a list, excluding pairs where items are the same,
using a nested loop approach.
"""

items = ["x", "y", "z"]
pairs = []

for i in items:
    for j in items:
        if i != j:
            pairs.append((i, j))

print(pairs)
