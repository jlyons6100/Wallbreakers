from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(numCourses)]
        n_map = defaultdict(int)
        for (c,p) in pre:
            adj[p].add(c)
            n_map[c] += 1
        q = []
        for c in range(numCourses):
            if not c in n_map:
                q.append(c)
        for course in q:
            for nei in adj[course]:
                n_map[nei] -= 1
                if n_map[nei] == 0:
                    q.append(nei)
        if len(q) != numCourses:
            return []
        return q
        
            
