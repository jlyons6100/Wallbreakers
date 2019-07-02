# Isomorphic Strings: Given two strings s and t, determine if they are isomorphic.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashh = {}
        for ind in range(len(s)):
            ltr = s[ind]
            if not ltr in hashh:
                if t[ind] in hashh.values():
                    return False
                hashh[ltr] = t[ind]
            else:
                if hashh[ltr] != t[ind]:
                    return False
        return True