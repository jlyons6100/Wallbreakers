class Solution:
    def helper(self, ind_s, ind_p):
        if (ind_s,ind_p) in self.cache:
            return self.cache[(ind_s,ind_p)]
        if ind_s == -1 and ind_p == -1:
            return True
        elif ind_p == -1 or ind_p < -1: 
            return False
        elif ind_s == -1:
            if self.p[ind_p] == "*":
                self.cache[(ind_s,ind_p -2)] = self.helper(ind_s, ind_p -2)
                return self.cache[(ind_s,ind_p -2)]
            else:
                return False
        elif self.p[ind_p] == '*':
            oneTrue = False
            p_val = self.p[ind_p - 1]
            pos_s = ind_s
            if p_val != ".":
                while(pos_s != -1 and self.s[pos_s] == p_val):
                    self.cache[(pos_s, ind_p - 1)] = self.helper(pos_s,ind_p - 1)
                    oneTrue = oneTrue or self.cache[(pos_s, ind_p - 1)]
                    pos_s = pos_s - 1
                self.cache[(ind_s, ind_p - 2)] = self.helper(ind_s, ind_p -2)
                oneTrue = oneTrue or self.cache[(ind_s, ind_p - 2)]
                return oneTrue
            else:
                while(pos_s != -1):
                    self.cache[(pos_s, ind_p - 1)] = self.helper(pos_s,ind_p - 1)
                    oneTrue = oneTrue or self.cache[(pos_s, ind_p - 1)]
                    pos_s = pos_s - 1
                self.cache[(ind_s, ind_p - 2)] = self.helper(ind_s, ind_p -2)
                oneTrue = oneTrue or self.cache[(ind_s, ind_p - 2)] 
                return oneTrue
                
        else: 
            if self.p[ind_p] == ".": # any letter
                self.cache[(ind_s - 1, ind_p - 1)] = self.helper(ind_s - 1, ind_p - 1)
                return self.cache[(ind_s - 1, ind_p - 1)]
            else: # specific letter
                if self.p[ind_p] == self.s[ind_s]:
                    self.cache[(ind_s - 1, ind_p - 1)] = self.helper(ind_s - 1, ind_p - 1)
                    return self.cache[(ind_s - 1, ind_p - 1)]
                else:
                    self.cache[(ind_s,ind_p)] = False
                    return False
            
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.cache = {}
        return self.helper(len(s)-1, len(p)-1)