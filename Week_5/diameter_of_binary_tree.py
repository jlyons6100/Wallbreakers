# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def height(self, node):
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
    def diam(self, node):
        if node == None:
            return 
        diam = self.height(node.left) + self.height(node.right)
        if diam > self.max:
            self.max = diam
        self.diam(node.left)
        self.diam(node.right)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        self.diam(root)
        return self.max
        # print(self.height(root.left))
        # print(self.height(root.right))