# Groups of Special Equivalent Strings: Given an array A of strings.
# Two strings are special equivalent if after any number of moves S == T

from collections import defaultdict
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = defaultdict(list)
        for string in A:
            even = ''
            odd = ''
            for i, ltr in enumerate(string):
                if i % 2 == 0:
                    even += ltr
                else:
                    odd += ltr 
            groups[("".join(sorted(even)),"".join(sorted(odd)))].append(string)
        return len(groups)
           
