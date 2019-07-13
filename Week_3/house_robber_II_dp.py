class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        var1 = 0
        var2 = 0
        var3 = 0
        var4 = 0
        for ind in range(len(nums) - 1):
            num1 = nums[ind]
            temp = var1
            var1 = max(var2+num1, var1)
            var2 = temp
            num2 = nums[ind + 1]
            temp = var3
            var3 = max(var4+num2, var3)
            var4 = temp
        return max(var1, var3)