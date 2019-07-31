class Solution:
    def bfs(self, g, i, colors, color):
        if i in colors:
            return color == colors[i]
        colors[i] = color
        self.done.add(i)
        for ind in g[i]:
            f = self.bfs(g, ind, colors, not color)
            if f == False:
                return f
        return True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        mmap = {}
        self.done = set()
        for i in range(len(graph)):
            if i not in self.done:
                f = self.bfs(graph, i, mmap, False)
                if f == False:
                    return False
        return True