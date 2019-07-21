from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = combinations([i for i in range(1, n+1)], k)
        return [list(tup) for tup in list(combs)]