# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def sums(self, node, pare):
        if node == None:
            return
        elif pare == 'l' and node.left == None and node.right == None:
            self.sum += node.val
        else:
            self.sums(node.left, 'l')
            self.sums(node.right, 'r')
            
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.sums(root, 'None')
        return self.sum