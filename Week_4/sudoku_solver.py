from collections import defaultdict
from copy import deepcopy
class Solution:
    def get_sub_box_num(self, row, col):
        if row < 3 and col < 3:
            return 1
        elif row < 3 and col < 6:
            return 2
        elif row < 3 and col < 9:
            return 3
        elif row >= 3 and row < 6 and col < 3:
            return 4
        elif row >= 3 and row < 6 and col < 6:
            return 5
        elif row >= 3 and row < 6 and col < 9:
            return 6
        elif row >= 6 and col < 3:
            return 7
        elif row >= 6 and col < 6:
            return 8
        elif row >= 6 and col < 9:
            return 9
    def recurs_solve(self, board, rows, cols, boxes, m, m_num):
        if m_num == -1:
            return True
        else:
            row, col = m[m_num]
            for num in range(1, 10):
                in_row = num in rows[row]
                in_col = num in cols[col]
                in_box = num in boxes[self.get_sub_box_num(row,col)]
                if  not in_row and not in_col and not in_box:
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[self.get_sub_box_num(row,col)].add(num)
                    board[row][col] = str(num)
                    sol = self.recurs_solve(board, rows, cols, boxes, m, m_num-1)
                    if sol == True:
                        return sol
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[self.get_sub_box_num(row,col)].remove(num)
            return False
            
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        m = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    rows[row].add(int(board[row][col]))
                    cols[col].add(int(board[row][col]))
                    boxes[self.get_sub_box_num(row,col)].add(int(board[row][col]))
                else:
                    board[row][col] = 'X'
                    m.append((row, col)) 
        m_num = len(m) - 1
        self.recurs_solve(board, rows, cols, boxes, m, m_num)

