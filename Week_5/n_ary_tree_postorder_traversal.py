"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        ret = []
        for child in root.children:
            ret.extend(self.postorder(child))
        return ret + [root.val]