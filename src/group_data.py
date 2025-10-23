# Groups a list of words by their first letter using itertools.groupby
# after sorting.

from itertools import groupby
from operator import itemgetter

words = ["avocado", "almond", "berry", "blackberry", "coconut"]
for key, group in groupby(sorted(words), key=itemgetter(0)):
    print(key, list(group))
