class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (not q and p) or (p.val != q.val):
            return False
        else:
            if not self.isSameTree(p.left, q.left)  or not self.isSameTree(p.right, q.right):
                return False
            return True