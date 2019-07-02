# Design Hashmap: Create a hashmap implementation in python.

class MyHashMap:
    def __init__(self):
        self.cap = 5000
        self.arr = [None] * self.cap
    def put(self, key: int, value: int) -> None:
        hval = hash(key) % self.cap
        if self.arr[hval] == None:
            self.arr[hval] = [(key, value)]
        else:
            for ind in range(len(self.arr[hval])):
                tup = self.arr[hval][ind]
                if tup[0] == key:
                    self.arr[hval][ind] = (key,value)
                    return
            self.arr[hval].append((key, value))
            
    def get(self, key: int) -> int:
        hval = hash(key) % self.cap
        if self.arr[hval] != None:
            for tup in  self.arr[hval]:
                if tup[0] == key:
                    return tup[1]
        return -1 
    def remove(self, key: int) -> None:
        hval = hash(key) % self.cap
        if self.arr[hval] != None:
            for ind in range(len(self.arr[hval])):
                if self.arr[hval][ind][0] == key:
                    del self.arr[hval][ind]
                    return
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
