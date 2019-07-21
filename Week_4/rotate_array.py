class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        ret = []
        cur = len(nums) - k
        for _ in range(len(nums)):
            ret.append(nums[cur])
            cur += 1
            if cur == len(nums):
                cur -= len(nums)
        for ind in range(len(nums)):
            nums[ind] = ret[ind]
    
        