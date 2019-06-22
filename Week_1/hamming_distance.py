# Hamming Distance:
# Returns the Hamming Distance between two integers(the number of positions at which the corresponding bits are different).

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s1 = "{0:b}".format(x).zfill(31) # Max of 2^31
        s2 = "{0:b}".format(y).zfill(31)
        ham = 0
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                ham += 1    
        return ham
        # List comprehension version, bad style to use because it creates an extra array?
        # return sum([1 for x in range(len(s1)) if s1[x] != s2[x]])