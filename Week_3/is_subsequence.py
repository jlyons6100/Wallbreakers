class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        elif len(t) == 0:
            return False
        cur = 0
        for ltr in t:
            if ltr == s[cur]:
                cur += 1
            if cur > len(s) -1:
                return True
        return False
                