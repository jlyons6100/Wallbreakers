from copy import deepcopy
class Solution:
    def recurs(self, recurs, cands, target, ans):
        new_recurs = []
        for cand in cands:
            for old in recurs:
                if sum(old) + cand == target:
                    copy = deepcopy(old)
                    copy.append(cand)
                    ans.append(copy)
                elif sum(old) + cand < target:
                    copy = deepcopy(old)
                    copy.append(cand)
                    # print(deepcopy(old).append(cand))
                    new_recurs.append(copy)
        if len(new_recurs) == 0:
            return 
        else: # recurs
            self.recurs(new_recurs, cands, target, ans)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        recurs = []
        
        for cand in candidates:
            if cand == target:
                ret.append([cand])
            if cand < target:
                recurs.append([cand])
        ret_not_perf = []
        self.recurs(recurs, candidates, target, ret_not_perf)
        ret_set = set()
        for i in ret:
            ret_set.add(tuple(sorted(i)))
        for i in ret_not_perf:
            ret_set.add(tuple(sorted(i)))
        return list(ret_set)