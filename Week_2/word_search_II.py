# Word Serach II: Find all words that are in a dictionary and on the board
class Node:
    def __init__(self):
        self.children = {}
    def in_children(self, val):
        return val in self.children
    def get_child(self, val):
        return self.children[val]
    def add_child(self, child_val):
        self.children[child_val] = Node()   
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        cur_node = self.root
        for ltr in word:
            if not cur_node.in_children(ltr):
                cur_node.add_child(ltr)
            cur_node = cur_node.get_child(ltr)
        cur_node.add_child(-1)       
    def search(self, word: str) -> bool:
        cur_node = self.root
        for ltr in word:
            if cur_node.in_children(ltr):
                cur_node  = cur_node.get_child(ltr)
            else:
                return False
        return cur_node.in_children(-1)
        
    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for ltr in prefix:
            if cur_node.in_children(ltr):
                cur_node  = cur_node.get_child(ltr)
            else:
                return False
        return True
class Solution:
    def search(self, row, col, myTrie, word, found, board, visited):
        if (row, col) in visited:
            return 
        visited.add((row,col))
        word += board[row][col]
        if myTrie.startsWith(word):
            if myTrie.search(word):
                print(word)
                found.add(word)
            if row - 1 >= 0:
                self.search(row - 1, col, myTrie, word, found, board, visited)
            if col - 1 >= 0:
                self.search(row, col - 1, myTrie, word, found, board, visited)
            if row + 1 < len(board):
                self.search(row + 1, col, myTrie, word, found, board, visited)
            if col + 1 < len(board[0]):
                self.search(row, col + 1, myTrie, word, found, board, visited)
        visited.remove((row, col)) 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        myTrie = Trie()
        for word in words:
            myTrie.insert(word)
        found = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                word = ""
                self.search(row, col, myTrie, word, found, board, set())
        return list(found)
            
            
            
            
            
            
            
            
            
            
            
        
        
