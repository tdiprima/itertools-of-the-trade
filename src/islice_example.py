# Demonstrating the use of itertools.islice() to slice iterables like generators.

from itertools import islice


def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1


print(list(islice(infinite_numbers(), 5, 10)))
# Output: [5, 6, 7, 8, 9]
