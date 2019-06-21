# Reverse Words In A String III:
# Reverse the order of characters in words in a sentence, preserve whitespace/initial word order.
class Solution:
	# reverse_word(word): Returns word with characters reversed
    def reverse_word(self, word:str) -> str:
        word = list(word)
        for ind in range(int(len(word)/2)):
            word[ind], word[len(word) - 1 - ind] = word[len(word) - 1 - ind], word[ind]
        return "".join(word)
    # reverseWords(s): Reverses each word in string s
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for ind in range(len(words)):
            words[ind] = self.reverse_word(words[ind])
        return " ".join(words)
        
        