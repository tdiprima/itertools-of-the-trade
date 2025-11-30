# Demonstrating the use of itertools.chain() to combine multiple iterables
# and flatten nested lists.

from itertools import chain

print(list(chain([1, 2], (3, 4), range(5, 7))))
# Output: [1, 2, 3, 4, 5, 6]

print(list(chain.from_iterable([[1, 2], [3, 4], [5]])))
# Output: [1, 2, 3, 4, 5]
