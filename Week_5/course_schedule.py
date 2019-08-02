from copy import deepcopy
class Node:
    def __init__(self, num):
        self.id = num
        self.children = []
    def __str__(self):
        return "Node: " + str(self.id) + " " + str(self.children)
class Solution: 
    def bfs(self, node):
        if node in self.cur:
            return False
        self.all.add(node)
        self.cur.add(node)
        for my_id in node.children:
            val = self.bfs(self.id_map[my_id])
            if val == False:
                return False
        self.cur.remove(node)
        return True
    def canFinish(self, nc: int, pre: List[List[int]]) -> bool:
        self.id_map = {}
        for node_id in range(nc):
            self.id_map[node_id] = Node(node_id)
        for tup in pre:
            self.id_map[tup[0]].children.append(tup[1])
        self.all = set()
        self.cur = set()
        for node_id in self.id_map:
            node = self.id_map[node_id]
            if not node in self.all:
                my_bool = self.bfs(node)
                if my_bool == False:
                    return False
                self.cur.clear()
        return True