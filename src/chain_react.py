"""
Blending itertools and functools for functional-style data processing.

This script:
1. Chains multiple iterables into one.
2. Filters out unwanted elements.
3. Maps a transformation over the results.
4. Reduces the final iterable into a single value.

Think of it like a mini, pure-Python data pipeline.
"""

import functools
import itertools
import operator

# --- Sample data ---
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

# --- Chain multiple iterables ---
all_nums = itertools.chain(nums1, nums2)

# --- Filter even numbers only ---
evens = filter(lambda x: x % 2 == 0, all_nums)

# --- Map a transformation (square each number) ---
squares = map(lambda x: x**2, evens)

# --- Reduce to a single sum using functools ---
total = functools.reduce(operator.add, squares)  # noqa: FURB179
# total = sum(squares)

# --- Display the pipeline result ---
print(f"Sum of squares of all even numbers: {total}")
