# Demonstrating the use of itertools.groupby() to group items by a key 
# after sorting (assuming sorted input).

from itertools import groupby

items = [
    ("fruits", "apple"),
    ("fruits", "banana"),
    ("veggies", "carrot"),
    ("veggies", "pea"),
]

for category, group in groupby(items, key=lambda x: x[0]):
    print(category, list(group))

# Output:
# fruits [('fruits', 'apple'), ('fruits', 'banana')]
# veggies [('veggies', 'carrot'), ('veggies', 'pea')]
