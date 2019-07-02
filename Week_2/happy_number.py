#. Happy Number: Algorithm to determine if a number is happy.
# A happy number is defined by the following process.
# Starting with any positive integer, replace the number
# by the sum of the squares of its digits and repeat the process
# until the number equals 1 or it loops endlessly.
class Solution:      
    def isHappy(self, n: int) -> bool:
        myset = set()
        new_n = -1
        while(True):
            new_n = sum([int(ltr)*int(ltr) for ltr in str(n)])
            n = new_n
            if n == 1:
                return True
            if not n in myset:
                myset.add(n)
            else:
                return False
        return False