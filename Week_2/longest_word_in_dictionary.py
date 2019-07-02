from collections import defaultdict

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
    def dfs_built(self, node, word):
        if len(node.children) == 0:
            return word
        else:
            temp = word
            for child_val in node.children:
                if child_val != -1:
                    child_children = node.get_child(child_val).children
                    if -1 in child_children:
                        myword = self.dfs_built(node.get_child(child_val), word + child_val)
                        if len(myword) > len(temp) or (len(myword) == len(temp) and myword < temp):
                            temp = myword
            return temp
class Solution:
    def longestWord(self, words: List[str]) -> str:
        myTrie = Trie()
        print(words)
        for word in words:
            myTrie.insert(word)
        return(myTrie.dfs_built(myTrie.root, ""))
        