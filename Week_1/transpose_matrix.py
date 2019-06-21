# Transpose Matrix:
# Flips rows and columns in a matrix

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ret = []
        for row in range(len(A[0])):
            ret.append([])
            for col in range(len(A)):
                ret[row].append(A[col][row])
        return ret