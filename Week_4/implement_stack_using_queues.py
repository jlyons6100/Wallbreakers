from queue import Queue
class MyStack:
    def __init__(self):
        self.q = Queue()
        self.head = None

    def push(self, x: int) -> None:
        self.head = x
        self.q.put(x)
        return
    
    def pop(self) -> int:
        new = Queue()
        if self.q.qsize() == 1:
            self.head = None
            return self.q.get()
        for _ in range(self.q.qsize()):
            val = self.q.get()
            if _ == self.q.qsize():
                return val
            elif _ == self.q.qsize() - 1:
                self.head = val
            self.q.put(val)
            
    def top(self) -> int:
        return self.head

    def empty(self) -> bool:
        return (self.q.qsize() == 0)