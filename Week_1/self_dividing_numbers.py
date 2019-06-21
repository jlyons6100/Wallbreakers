# Self Dividing Numbers:
# A Self-dividing number is a number that is divisible by every digit it contains. 
# Write a function to return an array of all of the self dividing numbers between a left and right bound inclusive.

class Solution:
	# is_self_div(num): Returns True if num is divisible by every digit it contains
    def is_self_div(self, num: int) -> bool:
        for ltr in str(num):
            if int(ltr) == 0 or num % int(ltr) != 0:
                return False
        return True

    # selfDividingNumbers(left,right): Returns array of all self dividing numbers between left and right inclusive.
    def selfDividingNumbers(self, left: int, right: int) -> List[int]: 
        return [num for num in range( left, right + 1) if self.is_self_div(num) ]