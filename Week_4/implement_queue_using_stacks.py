from queue import LifoQueue as Stack
class MyQueue:
    def __init__(self):
        self.q = Stack()
    def push(self, x: int) -> None:
        self.q.put(x)
    def pop(self) -> int:
        listt = []
        while (not self.q.empty()):
            listt.append(self.q.get())
        val = listt[len(listt) -1]
        del listt[len(listt) - 1]
        for x in range(len(listt)-1, -1, -1):
            self.q.put(listt[x])
        return val
    def peek(self) -> int:
        listt = []
        while (not self.q.empty()):
            listt.append(self.q.get())
        val = listt[len(listt) -1]
        for x in range(len(listt)-1, -1, -1):
            self.q.put(listt[x])
        return val
    def empty(self) -> bool:
        return self.q.qsize() == 0
        

