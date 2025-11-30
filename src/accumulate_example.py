# Demonstrating the use of itertools.accumulate() for running totals 
# and custom operations like multiplication.

import operator
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4])))
# Output: [1, 3, 6, 10]

print(list(accumulate([1, 2, 3, 4], operator.mul)))
# Output: [1, 2, 6, 24]
