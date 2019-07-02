# Word Search: Finds if a word exists in a board using DFS

class Solution:
    def word_exists(self, word: str, myset: set, row: int, col: int, board: List[List[str]]):
        tup = (row, col)
        if len(word) == 0: 
            return True
        elif word[0] == board[row][col] and not tup in myset:
            new_word = word[1:]
            if len(new_word) == 0:
                return True
            myset.add(tup)
            bools = set()
            if row - 1 >= 0:
                bools.add(self.word_exists(new_word, myset, row - 1, col, board))
            if row + 1 < len(board):
                bools.add(self.word_exists(new_word, myset, row + 1, col, board))
            if col -1 >= 0:
                bools.add(self.word_exists(new_word, myset, row, col - 1, board))
            if col + 1 < len(board[0]):
                bools.add(self.word_exists(new_word, myset, row, col + 1, board))
            if True in bools:
                return True
            myset.remove(tup)
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.word_exists(word, set(), row, col, board):
                        return True
        return False