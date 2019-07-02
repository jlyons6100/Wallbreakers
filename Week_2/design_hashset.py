# Design Hashset: Create a hashset implementation in python.

class MyHashSet:
    def __init__(self):
        self.capacity = 3750 
        self.arr = [None] * self.capacity 
    def add(self, key: int) -> None:
        hval = hash(key) % self.capacity
        if self.arr[hval] == None:
            self.arr[hval] = [key]
        else:
            if key not in self.arr[hval]:
                self.arr[hval].append(key)
                
    def remove(self, key: int) -> None:
        hval = hash(key) % self.capacity
        if self.arr[hval] == None:
            return
        for ind in range(len(self.arr[hval])):
            if self.arr[hval][ind] == key:
                del self.arr[hval][ind]
                return
    def contains(self, key: int) -> bool:
        hval = hash(key) % self.capacity
        if self.arr[hval] == None:
            return False
        else:
            for h_key in self.arr[hval]:
                if h_key == key:
                    return True
            return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)