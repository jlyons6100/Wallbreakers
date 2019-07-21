import queue
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        most_common = freqs.most_common(k)
        return [pair[0] for pair in most_common]