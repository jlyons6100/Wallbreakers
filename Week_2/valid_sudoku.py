# Valid Sudoku: Determine if a 9x9 Sudoku board is valid.

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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        sub_boxes = {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    box_ind = self.get_sub_box_num(row, col)
                    if box_ind not in sub_boxes:
                        sub_boxes[box_ind] = set(board[row][col])
                    else:
                        if board[row][col] in sub_boxes[box_ind]:
                            return False
                        else:
                            sub_boxes[box_ind].add(board[row][col])
                    if row not in rows:
                        rows[row] = set(board[row][col])
                    else:
                        if board[row][col] in rows[row]:
                            return False
                        else:
                            rows[row].add(board[row][col])
                    if col not in cols:
                        cols[col] = set(board[row][col])
                    else:
                        if board[row][col] in cols[col]:
                            return False
                        else:
                            cols[col].add(board[row][col])
        return True