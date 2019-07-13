class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([min(nums[x], nums[x+1]) for x in range(0, len(nums)-1, 2) ])