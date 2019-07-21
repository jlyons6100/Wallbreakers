class Solution:
	# This would generate all permutations, but that's not what this question asks for
    # def combo(self, cur, n, ret, arr):
    #     if cur == n:
    #         arr.append(ret)
    #         return
    #     self.combo(cur+1, n, ret + "1", arr)
    #     self.combo(cur+1, n, ret + "0", arr)  
    def combo(self, n):
        if n == 0:
            return ['0']
        elif n == 1:
            return ['0','1']
        else:
            prev = self.combo(n-1)
            new = []
            for combo in prev:
                new.append('0' + combo)
            prev.reverse()
            for combo in prev:
                new.append('1' + combo)
            return new
    def grayCode(self, n: int) -> List[int]:
        combo = self.combo(n)
        ret = []
        for c in combo:
            ret.append(int(c, 2))
        return ret
       