# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pop_seq(self, node, seq): # populate sequenece
        if node == None:
            return
        elif node.left == None and node.right == None:
            seq.append(node.val)
        else:
            self.pop_seq(node.left, seq)
            self.pop_seq(node.right, seq)
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        r1seq = []
        r2seq = []
        self.pop_seq(root1, r1seq)
        self.pop_seq(root2, r2seq)
        return r1seq == r2seq
    
        
        