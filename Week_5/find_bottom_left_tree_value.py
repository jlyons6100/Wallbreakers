class Solution:
    def l_val(self, node, depth):
        if node == None:
            return
        if depth > self.cur_depth:
            self.cur_depth = depth
            self.cur_val = node.val
        self.l_val(node.left, depth + 1)
        self.l_val(node.right, depth + 1)
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.cur_depth = -1
        self.cur_val = -1
        self.l_val(root, 0)
        return self.cur_val