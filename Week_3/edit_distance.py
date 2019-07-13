class Solution(object):
    def helper(self, m, n):
        if (m,n) in self.cache: return self.cache[(m,n)]
        if m == 0 or n == 0: return max(m, n)
        elif self.w1[m - 1] == self.w2[n - 1]:
            self.cache[(m-1,n-1)] = self.helper(m-1, n-1)
            return 0 + self.cache[(m-1,n-1)]
        else:
            self.cache[(m-1, n)] = self.helper(m-1, n) # insert
            self.cache[(m,n-1)] = self.helper(m, n-1) # delete
            self.cache[(m-1, n-1)] = self.helper(m-1, n-1)  # modify
            return 1 + min(self.cache[(m-1, n)], self.cache[(m,n-1)], self.cache[(m-1, n-1)])
    def minDistance(self, w1, w2): 
        self.cache = {}
        self.w1 = w1
        self.w2 = w2
        return self.helper(len(w1), len(w2))