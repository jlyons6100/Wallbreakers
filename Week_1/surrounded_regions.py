# Surrounded Regions:
# Given a 2D board containing X and O, capture all the regions surrounded by "X"

class Solution:
    # recurs_connect: Builds set of connected O's starting from border
    def recurs_connect(self, board, row, col, connected): 
        if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and board[row][col] == "O" and not (row,col) in connected:
            connected.add((row, col))
            # Cells are connected horizontally or vertically
            self.connect_graph(board, row - 1, col, connected)
            self.connect_graph(board, row + 1, col, connected)
            self.connect_graph(board, row, col - 1, connected)
            self.connect_graph(board, row, col + 1, connected)
    # solve(board):Turns O's that aren't on the border or connected to border O's into X's
    def solve(self, board: List[List[str]]) -> None:
        if board == []: return
        row_l = 0
        row_r = len(board) - 1
        connected = set()
        for col in range(len(board[0])):
            if board[row_l][col] == "O":
                self.connect_graph(board, row_l, col, connected)
            if board[row_r][col] == "O":
                self.connect_graph(board, row_r, col, connected)
        col_l = 0
        col_r = len(board[0]) - 1
        for row in range(len(board)):
            if board[row][col_l] == "O":
                self.connect_graph(board, row, col_l, connected)
            if board[row][col_r] == "O":
                self.connect_graph(board, row, col_r, connected)
        for row in range(len(board) - 1):
            for col in range(len(board[0]) - 1):
                if board[row][col] == "O" and not (row,col) in connected:
                    board[row][col] = "X"