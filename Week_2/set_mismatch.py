from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter()
        for num in nums:
            freq[num] += 1
        repeat = freq.most_common(1)[0][0]
        for x in range(1, len(nums) + 1): 
            if freq[x] == 0:
                return [repeat, x]