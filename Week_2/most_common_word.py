# Most Common Word: Most common words from a paragraph

import re
from collections import defaultdict, Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freqs = Counter()
        b_set = set(banned)
        p_list = re.split('[ ,|\.!?;\']',paragraph)
        for word in p_list:
            l = word.lower()
            if  word != "" and l not in b_set:
                freqs[l] += 1
        return freqs.most_common(1)[0][0]
        
    
        