# Groups of Special Equivalent Strings: Given an array A of strings.
# Two strings are special equivalent if after any number of moves S == T
from collections import Counter, defaultdict
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = defaultdict(list)
        for word in A:
            even = Counter([word[ind] for ind in range(len(word)) if ind % 2 == 0])
            odd = Counter([word[ind] for ind in range(len(word)) if ind % 2 == 1])
            f_e = frozenset(even.items())
            f_o = frozenset(odd.items())
            tup = (f_e, f_o)
            groups[tup].append(word)
        return len(groups)
           