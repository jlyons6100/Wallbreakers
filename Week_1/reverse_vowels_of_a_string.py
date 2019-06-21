# Reverse Vowels of A String:
# Takes a string as input and reverses only the vowels in the string

class Solution:
    # is_vowel(letter): Returns true if a letter is a vowel
    def is_vowel(self, letter: str) -> bool:
        a = letter.lower() == "a"
        e = letter.lower() == "e"
        i = letter.lower() == "i"
        o = letter.lower() == "o"
        u = letter.lower() == "u"
        return a or e or i or o or u
    # reverseVowels(s): Swaps positions of vowels in a string
    def reverseVowels(self, s: str) -> str:
        x = 0
        y = len(s) - 1
        s = list(s)
        while (x < y):
            while(x < len(s) and not self.is_vowel(s[x])):
                x += 1
            while(y >= 0 and not self.is_vowel(s[y])):
                y -= 1
            if not x < len(s) or not y >= 0 or not x < y: 
                break
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
        return "".join(s)
