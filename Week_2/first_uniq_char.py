# First Uniq Char: First unique character in a string

import sys
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        first_seen = {}
        for ind in range(len(s)):
            ltr = s[ind]
            if not ltr in freq:
                freq[ltr] = 1
                first_seen[ltr] = ind 
            else:
                freq[ltr] += 1
        index = sys.maxsize
        for ltr in freq:
            if freq[ltr] == 1:
                if first_seen[ltr] < index: 
                    index = first_seen[ltr]
        if index == sys.maxsize:
            return -1
        else:
            return index
