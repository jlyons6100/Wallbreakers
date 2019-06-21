# Fizz Buzz:
# Outputs the string representations of numbers from 1 to n. Special strings for multiples of 5 and 3

class Solution:
    # fizzBuzz(n): Returns array of strings between 1 and n.
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if x % 5 == 0 and x % 3 == 0
                else 'Fizz' if  x % 3 == 0 
                else 'Buzz' if  x % 5 == 0 
                else str(x) for x in range(1, n+1)]