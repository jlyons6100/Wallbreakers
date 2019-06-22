# Valid Anagram: A function to determine if t is an anagram of s
class Solution:
    # freq_map(string): Returns a dict for the frequencies of characters in a string
    def freq_map(self, string:str) -> dict:
        freq = {}
        for ltr in string:
            if not ltr in freq:
                freq[ltr] = 1
            else:
                freq[ltr] += 1
        return freq
    # isAnagram(s, t): Returns true if s is an anagram of t, uses dicts
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.freq_map(s)
        t_map = self.freq_map(t)
        return s_map == t_map
                        
        