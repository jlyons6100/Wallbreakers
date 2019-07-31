from copy import deepcopy
class Solution:
    def bfs(self, cord, m):
        self.cache.add(cord)
        if m[cord[0]][cord[1]] == 0:
            return True
        if cord in self.visited:
            print(cord)
            return False
        self.visited.add(cord)
        for x in range(self.numCourses):
            if x != cord[0]:
                val = self.bfs((x, cord[0]), m)
                if val == False:
                    return False
        return True
        
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        m = []
        self.cache = set()
        self.numCourses = numCourses
        for _ in range(numCourses):
            l = []
            for __ in range(numCourses):
                l.append(0)
            m.append(l)
        for tup in pre:
            m[tup[0]][tup[1]] = 1
        self.visited = set()
        for row in range(len(m)):
            for col in range(len(m[0])):
                cord = (row, col)
                val = True
                if m[row][col] != 0 and cord not in self.cache:
                    val = self.bfs(cord, m)
                if val == False:
                    return False
                self.visited = set()
        return True
        
            