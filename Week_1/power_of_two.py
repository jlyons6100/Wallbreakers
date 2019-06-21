# Power of Two:
# Returns True if n is a power of 2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            while (n != 1):
                n = n / 2
                if n != int(n):
                    return False
            return n == 1