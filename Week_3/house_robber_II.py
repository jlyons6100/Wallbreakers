class Solution:
    def helper(self, nums, i, end):
        if str(i)+" "+str(end) in self.memo:
            return self.memo[str(i)+" "+str(end)]
        if i < end:
            return 0
        else:
            rob_cur = self.helper(nums, i - 2, end) + nums[i]
            no_rob = self.helper(nums, i - 1, end)
            maxx = max(rob_cur,no_rob)
            self.memo[str(i)+" "+str(end)] = maxx
            return maxx
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        if len(nums) == 1:
            return nums[0]
        no_first = self.helper(nums,len(nums) - 2, 0)
        first = self.helper(nums,len(nums) - 1, 1)
        return max(no_first, first)