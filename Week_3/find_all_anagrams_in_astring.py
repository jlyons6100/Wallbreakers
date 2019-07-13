import bisect
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) == 0 or len(s) == 0:
            return []
        l_p = sorted(p)
        l_s = sorted(s[:len(p)])
        ind_arr = set()
        for ind in range(len(s) - len(p)+1):
            if l_p == l_s:
                ind_arr.add(ind)
            sub = s[ind]
            del l_s[bisect.bisect_left(l_s, sub)]
            try:         
                add = s[ind +len(p)]
                bisect.insort_left(l_s, add)
            except:
                break
        if l_p == l_s and ind not in ind_arr:
            ind_arr.add(ind)
        return list(ind_arr)
            
            
            