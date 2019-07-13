class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True) 
        s.sort(reverse=True)
        ind_s = 0
        accum = 0
        for ind_g in range(len(g)):
            if ind_s >= len(s):
                break
            if  g[ind_g] <= s[ind_s]:
                accum += 1
                ind_s += 1
        return accum
        