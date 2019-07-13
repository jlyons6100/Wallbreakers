class Solution:
    def search(self, nums: List[int], t: int) -> int:
        beg = 0
        end = len(nums) - 1
        mid = int((beg + end)/2)
        while(beg <= end):
            if nums[mid] > t:
                end = mid - 1
                mid = int((beg + end)/2)
            elif nums[mid]  < t:
                beg = mid + 1
                mid = int((beg + end)/2)
            else:
                return mid
        if nums[mid] == t:    
            return mid
        else:
            return -1
        