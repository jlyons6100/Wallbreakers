# Two Sum: Returns indicces of two numbers that add up to target
class Solution:
    
    # index_map(nums): Map of value to index
    def index_map(self, nums: List[int]) -> dict:
        indices = {}
        for ind in range(len(nums)):
            if not nums[ind] in indices:
                indices[nums[ind]] = [ind]
            else:
                indices[nums[ind]].append(ind)
        return indices
    # twoSum(nums, target): Returns indicces of two numbers that add up to target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = self.index_map(nums)
        for value in indices:
            if target - value in indices:
                if value != target-value:
                    return [indices[value][0], indices[target-value][0]]
                else:
                    if len(indices[value]) > 1:
                        return [indices[value][0], indices[value][1]]
                        
        