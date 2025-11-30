# Demonstrating the use of itertools.cycle() to create an infinite cycle of elements,
# with a break condition.

from itertools import cycle

counter = 0
for color in cycle(["red", "green", "blue"]):
    print(color)
    counter += 1
    if counter == 6:
        break

# Output:
# red
# green
# blue
# red
# green
# blue
