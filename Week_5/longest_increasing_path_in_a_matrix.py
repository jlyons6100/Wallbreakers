class Solution:
    def bfs(self, m, r, c, lenn):
        if (r, c) in self.cache:
            return lenn + self.cache[(r,c)] - 1
        cur = m[r][c]
        l = ri = u = d = 0
        if r - 1 >= 0 and m[r - 1][c] > cur:
            l = self.bfs(m, r - 1, c, lenn+1)
        if r + 1 < len(m) and m[r + 1][c] > cur:
            ri = self.bfs(m, r + 1, c, lenn+1)
        if c - 1 >= 0 and m[r][c - 1] > cur:
            u = self.bfs(m, r, c - 1, lenn+1)
        if c + 1 < len(m[0]) and m[r][c + 1] > cur:
            d = self.bfs(m, r, c + 1, lenn+1)
        if l == 0 and ri == 0 and u == 0 and d == 0:
            return lenn
        self.cache[(r,c)] = max(l, ri, u, d) - lenn + 1 
        return max(l, ri, u, d)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxx = 0
        self.cache = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.cache[(row, col)] = self.bfs(matrix, row, col, 1)
                maxx = max(maxx, self.cache[(row, col)])
        return maxx