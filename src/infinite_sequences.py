# Shows how to create and slice infinite sequences using itertools.count,
# cycle, and islice.

from itertools import count, cycle, islice

# Count upwards from 5
numbers = islice(count(5), 5)
print(list(numbers))  # [5, 6, 7, 8, 9]

# Cycle through values
shades = ["dark", "light", "medium"]
cycled_shades = islice(cycle(shades), 8)

print(
    list(cycled_shades)
)  # ['dark', 'light', 'medium', 'dark', 'light', 'medium', 'dark', 'light']
