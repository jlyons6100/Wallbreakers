# Uncommon Words From Sentences: Words that only exist in one sentence

from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        l_A = A.split(" ")
        l_B = B.split(" ")
        count = Counter(l_A)
        count.update(l_B)
        return [key for key in count if count[key] == 1]