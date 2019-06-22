# Single Number: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution:
    # singleNumber(nums): Finds single element in a non-empty array of integers by XORing numbers together
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for n in nums: # number ^ number equals 0, 
            x ^= n
        return x