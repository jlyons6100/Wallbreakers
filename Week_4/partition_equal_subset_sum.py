class Solution:
    def can_partition(self, nums, half_sum, sack, i):
        if sack in self.cache:
            return self.cache[sack]
        if i > len(nums) - 1:
            return sack == half_sum
        if sack > half_sum:
            return False
        elif sack == half_sum:
            return True
        else:
            incld = self.can_partition(nums, half_sum, sack + nums[i], i+1)
            excld = self.can_partition(nums, half_sum, sack, i+1)
            self.cache[sack] = incld or excld
            return incld or excld
    def canPartition(self, nums: List[int]) -> bool:
        self.cache = {}
        accum = 0
        maxx = 0
        for x in nums:
            accum += x
            maxx = max(maxx, x)
        nums.sort(reverse = True)
        half_sum = accum / 2
        if maxx > half_sum:
            return False
        if not half_sum.is_integer():
            return False
        else:
            sack = 0
            index = 0
            return self.can_partition(nums, int(half_sum), sack, index)