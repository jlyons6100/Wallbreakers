# Unique Morse Representations: Return the number of different morse code transformations among all the words we have.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        freq = {}
        for word in words:
            m_word = ""
            for letter in word:
                m_word += code[ord(letter) - ord("a")]
            if m_word in freq:
                freq[m_word] += 1
            else:
                freq[m_word] = 1
        return len(freq)