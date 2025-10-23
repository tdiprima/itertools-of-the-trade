# Generates permutations and combinations of players
# using itertools for team or pairing scenarios.

from itertools import combinations, permutations

players = ["Alex", "Jordan", "Taylor"]

# all possible ordered pairs
print(list(permutations(players, 2)))

# all unique pairs (order doesn't matter)
print(list(combinations(players, 2)))
