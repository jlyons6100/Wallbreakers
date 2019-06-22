# Friend Circles: Given an N*N matrix representing the friend relationship between students in the class, output the total number of friend circles.
class Solution:
    # recurs_add(myset, row, M): Recursively adds friends to the group
    def recurs_add(self, myset, row, M):
        myset.add(row)
        for col in range(len(M[0])):
            if  col not in myset and M[row][col] == 1: 
                myset.add(col)
                self.recurs_add(myset, col, M)
    # findCircleNum(M): Finds total number of friend groups
    def findCircleNum(self, M: List[List[int]]) -> int:
        myset = set()
        count  = 0
        for row in range(len(M)):
            if row not in myset:
                count +=1 
                self.recurs_add(myset,row, M)
        return count