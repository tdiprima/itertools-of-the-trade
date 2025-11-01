# Reads the first N lines from a file called "datafile" and prints them.
# https://stackoverflow.com/questions/1767513/read-first-n-lines-of-a-file-in-python
from itertools import islice, product

# TODO: BASH!
# head -n 501 fifa_data.csv > output.csv

N = 100

with open("datafile") as my_file:
    head = [next(my_file) for x in range(N)]
print(head)

# or

with open("datafile") as my_file:
    head = list(islice(my_file, N))
print(head)

exit(0)


# ------------
# https://medium.com/codrift/the-hidden-python-features-that-feel-like-cheat-codes-0151fd2c17e0
# itertools for Automation at Scale

colors = ["red", "green"]
sizes = ["S", "M", "L"]

for combo in product(colors, sizes):
    print(combo)
