# Prefix in All:
# Finds the longest common prefix string amongst an array of strings. 

class Solution:
    # prefix_in_all(strs, prefix): Returns true if a prefix is in every string
    def prefix_in_all(self, strs:List[str], prefix: str):
        for strr in strs:
            if strr[:len(prefix)] != prefix:
                return False
        return True
    # longestCommonPrefix(strs, prefix): Returns longest common prefix of strings in strs
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for x in range(len(strs[0]), 0, -1):
            pre = strs[0][:x]
            if self.prefix_in_all(strs, pre):
                return pre
        return ""