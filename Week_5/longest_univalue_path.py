class Solution:
    def depth(self, node, val):
        if node == None:
            return 0
        elif node.val != val:
            return 0
        else:
            return 1+ max(self.depth(node.left, val), self.depth(node.right, val))
    def longest_path(self, root):
        if root == None:
            return
        else:
            val = root.val
            d =  self.depth(root.left, val) + self.depth(root.right, val)
            if d > self.max:
                self.max = d
            self.longest_path(root.left)
            self.longest_path(root.right)
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            self.max = 0
            self.longest_path(root)
        return self.max