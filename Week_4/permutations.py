import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = itertools.permutations(nums)
        perm_list = list(perms)
        return [i for i in perm_list]