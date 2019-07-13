class Solution:
    def helper(self, x: float, n: int):
        if str(x) + " "+str(n) in self.cache:
            return self.cache[str(x) + " "+str(n)]
        if n == 0:
            return 1
        else:
            if n % 2 == 0:
                res = self.myPow(x, n//2) 
                self.cache[str(x) + " "+str(int(n))] = res* res
                return res * res
            else:
                res =  self.myPow(x, n//2)
                self.cache[str(x) + " "+str(int(n))] = res * res * x
                return res*res*x
    def myPow(self, x: float, n: int) -> float:
        self.cache = {}
        if n >= 0:
            return self.helper(x,n)
        else:
            return 1 / self.helper(x, -n)
                
        
        