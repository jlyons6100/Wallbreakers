# Jewels and Stones: Given strings J representing the types of stones that are jewels and s representing the stones you have.
# Determine how many stones you have that are also jewels.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set = set()
        for jewel in J:
            j_set.add(jewel)
        count = 0
        for stone in S:
            if stone in j_set:
                count += 1
        return count