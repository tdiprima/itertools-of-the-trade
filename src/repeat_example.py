# Demonstrating the use of itertools.repeat() to generate repeated values, 
# including in combination with zip().

from itertools import repeat

print(list(repeat("Hi", 3)))
# Output: ['Hi', 'Hi', 'Hi']

print(list(zip(range(5), repeat(0))))
# Output: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
