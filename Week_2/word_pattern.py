# Word Pattern: Given a pattern and a string str, find if str follows the same pattern.

class Solution:
    # wordPattern(p, s): Using a pattern s and string s, 
    #compares the order of frequency counts in both, to find if str follows the same pattern
    def wordPattern(self, p: str, s: str) -> bool:
        freq_p = {}
        arr_p = []
        for ltr in p:
            if not ltr in arr_p:
                arr_p.append(ltr)
            if not ltr in freq_p:
                freq_p[ltr] = 1
            else:
                freq_p[ltr] += 1

        arr_s = []
        freq_s = {}
        for word in s.split(" "):
            if not word in arr_s:
                arr_s.append(word)
            if not word in freq_s:
                freq_s[word] = 1
            else:
                freq_s[word] += 1

        if len(arr_p) == len(arr_s): # Same number of unique values
            for ind in range(len(arr_p)): 
                if freq_p[arr_p[ind]]  != freq_s[arr_s[ind]]: # Values have same order
                    return False
            return True
        return False