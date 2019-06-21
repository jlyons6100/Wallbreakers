# Detect Capital:
# Judges whether the usage of capitals in a word is right or not.
# Usage of capitals of a word is right when:
# 1. All the letters are capital
# 2. All the letters are not capital
# 3. Only the first letter in this word is capital. 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower()  or (word[0].isupper() and word[1:].islower()) 
        