"""
A functional-style data pipeline built using itertools + functools.

This script demonstrates:
  • Combining iterables with itertools.chain
  • Filtering + mapping transformations
  • Grouping similar values with itertools.groupby
  • Applying multiple-argument functions via itertools.starmap
  • Accumulating running totals with itertools.accumulate
  • Reducing everything down using functools.reduce

Result: A clean, Pythonic example of lazy evaluation and iterator composability.
"""

import functools
import itertools
import operator
from operator import itemgetter
from random import randint

# --- Generate some sample data ---
# Simulate two lists of (category, value) pairs
data1 = [("A", randint(1, 5)) for _ in range(5)]  # nosec B311
data2 = [("B", randint(1, 5)) for _ in range(5)]  # nosec B311
data3 = [("A", randint(1, 5)) for _ in range(5)]  # nosec B311

# --- Chain all data sources together ---
all_data = itertools.chain(data1, data2, data3)

# --- Sort so groupby will work properly ---
sorted_data = sorted(all_data, key=itemgetter(0))

# --- Group by category ---
grouped = itertools.groupby(sorted_data, key=itemgetter(0))


# --- For each group, sum the values using starmap + accumulate ---
def process_group(group):
    cat, items = group
    values = [v for _, v in items]

    # Use accumulate to show running totals
    running_totals = list(itertools.accumulate(values))
    total = functools.reduce(operator.add, values)  # noqa: FURB179

    return (cat, values, running_totals, total)


processed = itertools.starmap(process_group, grouped)

# --- Display results ---
for cat, values, running, total in processed:
    print(f"\nCategory {cat}:")
    print(f"  Values: {values}")
    print(f"  Running totals: {running}")
    print(f"  Final total: {total}")
