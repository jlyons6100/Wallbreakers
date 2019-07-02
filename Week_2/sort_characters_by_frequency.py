# Sort Characters By Frequency: Given a string sort it in decreasing order based on
# frequency of characters.
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for ltr in s:
            d[ltr] += 1
        # print(d.items())
        sorted_x = sorted(d.items(), key=lambda kv: kv[1])
        sorted_x.reverse()
        strr = ""
        for tup in sorted_x:
            for i in range(tup[1]):
                strr += tup[0]
        return (strr)