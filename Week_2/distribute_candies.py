# Distribute Candies: Given an integer array with even length, where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister.

from collections import Counter
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(int(len(candies) / 2), len(Counter(candies)))
        
            
            
            