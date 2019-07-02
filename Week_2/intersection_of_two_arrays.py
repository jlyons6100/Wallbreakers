# Intersection of Two Arrays: Write a function to compute intersection of two arrays

from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = Counter(nums1) & Counter(nums2)
        return [key for key in inter]