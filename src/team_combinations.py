# Generates permutations and combinations of players
# using itertools for team or pairing scenarios.

from itertools import combinations, permutations

players = ["Alex", "Jordan", "Taylor"]
print(list(permutations(players, 2)))
print(list(combinations(players, 2)))
