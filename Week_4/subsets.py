from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cmbs = combinations(nums,3)
        ret = [[]]
        for n in range(1 , len(nums)+1):
            cmb_list = list(combinations(nums, n))
            for tup in cmb_list:
                ret.append(list(tup))
        return ret