class Solution:
    def bfs(self, b, r, c, visited, i, word):
        tup = (r, c)
        if tup in visited:
            return False
        if i == len(word) - 1 and b[r][c] == word[i]:
            return True
        else:
            l = False
            ri = False
            u = False
            d = False
            if b[r][c] == word[i]:
                visited.add(tup)
                if r - 1 >= 0:
                    l = self.bfs(b, r - 1, c, visited, i+1, word)
                    if l:
                        return True
                if r + 1 < len(b):
                    ri = self.bfs(b, r + 1, c, visited, i+1, word)
                    if ri:
                        return True
                if c - 1 >= 0:
                    u = self.bfs(b, r, c - 1, visited, i+1, word)
                    if u:
                        return u
                if c + 1 < len(b[0]):
                    d = self.bfs(b, r, c + 1, visited, i+1, word)
                    if d:
                        return d
                visited.remove(tup)    
            return l or ri or u or d
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                # print(board[r][c])
                if board[r][c] == word[0]:
                    if self.bfs(board, r, c, set(), 0, word):
                        return True
        return False