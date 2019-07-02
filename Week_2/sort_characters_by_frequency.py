# Sort Characters By Frequency: Given a string sort it in decreasing order based on
# frequency of characters.
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ret = c.most_common(len(c))
        return "".join([tup[0]*tup[1] for tup in ret])
