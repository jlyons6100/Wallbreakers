from copy import deepcopy
class Node:
    def __init__(self, num):
        self.id = num
        self.children = []
    def __str__(self):
        return "Node: " + str(self.id) + " " + str(self.children)
class Solution:
    
    def bfs(self, node, search):
        print(node.id)
        print(self.cur)
        # print(search)
        if node.id in self.cur:
            return False
        search.remove(node.id) 
        self.cur.add(node.id)
        self.myOrder.append(node.id)
        if len(search) == 0:
            return True
        for child_id in node.children:
            val = self.bfs(self.map[child_id], deepcopy(search))
            if val == True:
                return True
        self.cur.remove(node.id)
        
        
        return False
        
        
    def findOrder(self, nc: int, pre: List[List[int]]) -> List[int]:
        self.map = {}
        for nid in range(nc):
            self.map[nid] = Node(nid)
        for tup in pre:
            self.map[tup[1]].children.append(tup[0])
        
        any_order = []
        search = set()
        for nid in self.map:
            if len(self.map[nid].children) != 0:
                search.add(self.map[nid].id)
                for node in self.map[nid].children:
                    search.add(node) 
        for nid in self.map:
            if self.map[nid].id not in search:
                any_order.append(self.map[nid].id)
        
        self.cur = set()
        self.myOrder = []
        if len(search) == 0:
            return any_order
        for nid in search:
            val = self.bfs(self.map[nid], deepcopy(search))
            print("END")
            if val == True:
                return self.myOrder + any_order
            self.myOrder.clear()
            self.cur.clear()
                
        return []

