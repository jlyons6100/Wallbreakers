# Binary Gap: Finds the longest distance between two consecutive 1's in the binary representation of N

class Solution:
    def binaryGap(self, N: int) -> int:
        bits =  "{0:b}".format(N)
        pat = False # True when you have seen a one
        maxx = 0 # Longest distance
        dis = 0 # Current distance
        for ind in range(len(bits)):
            if not pat: 
                if bits[ind] == "1":
                    pat = True
            else: # Looking for the last one in a series of two consecutive 1's
                dis += 1
                if bits[ind] == "1":
                    if dis > maxx: maxx = dis
                    dis = 0
        return maxx