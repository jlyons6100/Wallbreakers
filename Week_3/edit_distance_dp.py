class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = []
        for i in range(m+1):
            arr = [0 for i in range(n+1)]
            dp.append(arr)
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    ins = dp[i][j-1]
                    dell = dp[i-1][j]
                    mod = dp[i-1][j-1]
                    dp[i][j] = 1 + min(ins, dell, mod)
        return dp[m][n]
        