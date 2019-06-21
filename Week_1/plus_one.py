# Plus One:
# Adds one to a list representing a number

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = len(digits) - 1 # Last digit
        if digits[cur] < 9:
            digits[cur] += 1
        else:
            while(cur != -1 and digits[cur] == 9):
                digits[cur] = 0
                cur -= 1
            if cur == -1: 
                digits.insert(0,1)
            else: 
                digits[cur] += 1
        return digits