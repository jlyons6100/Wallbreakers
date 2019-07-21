class Solution:
    def helper(self, left, right, combo, ret):
        if left == 0 and right == 0:
            ret.append(combo)
        if left > 0:
            self.helper(left-1, right+1, combo +"(", ret)
        if right > 0:
            self.helper(left, right - 1, combo + ")", ret)
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.helper(n, 0, "", ret)
        return ret