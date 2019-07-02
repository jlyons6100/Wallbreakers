# Find All Anagrams in a String: Given a string s and a non-empty string p
# find all the start indices of p's anagrams in s
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntp = Counter(p)
        cnts = Counter(s[:len(p)])
        ret = []
        if cntp == cnts:
                ret.append(0)
        for ind in range((len(s) - len(p))):
            cnts[s[ind]] -= 1
            if cnts[s[ind]] == 0:
                del cnts[s[ind]]
            cnts[s[ind+len(p)]] +=1
            if cntp == cnts:
                ret.append(ind+1)
        return(ret)
            
            
            