class Solution:
    def helper(self, nums, k_sum, sacks, i):
        if frozenset(sacks)  in self.cache:
            return self.cache[frozenset(sacks)]
        solution = True
        for summ in sacks:
            if summ != k_sum:
                solution = False
        if solution == True:
            return True
        else:
            for n in range(len(sacks)):
                if sacks[n] + nums[i] <= k_sum:
                    sacks[n] += nums[i]
                    val = self.helper(nums, k_sum, sacks, i+1)
                    self.cache[frozenset(sacks)] = val
                    if val == True:
                        return True
                    sacks[n] -= nums[i]
            return False
    def canPartitionKSubsets(self, nums, k):
        self.cache = {}
        k_sum = sum(nums) / k
        if not k_sum.is_integer() or k > len(nums):
            return False
        else:
            sacks = [0]*k
            nums.sort(reverse = True)
            # print(k_sum)
            # if nums[len(nums) - 1] > k_sum: return False
            return self.helper(nums, int(k_sum), sacks, 0)