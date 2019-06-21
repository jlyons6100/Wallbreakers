# Is Palindrome:
# Returns true if a string is a  palindrome, considering only alphanumeric characters and ignoring cases 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        y = len(s) - 1
        while(x < y):
            while(x < len(s) and not s[x].isalnum()):
                x += 1
            while(y >= 0 and  not s[y].isalnum()):
                y -= 1
            if not x < len(s) or not y >= 0: 
                return True
            if s[x].lower() != s[y].lower():
                return False
            x += 1
            y -= 1
        return True
