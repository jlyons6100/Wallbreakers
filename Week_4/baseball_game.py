from queue import LifoQueue as Stack
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = Stack()
        accum = 0
        for op in ops:
            try:
                stack.put(int(op))
                accum += int(op)
            except:
                if op == 'C':
                    last_valid = stack.get()
                    accum -= last_valid
                elif op == 'D':
                    last_valid = stack.get()
                    accum += last_valid*2
                    stack.put(last_valid)
                    stack.put(last_valid*2)
                elif op == "+":
                    last_valid = stack.get()
                    before_last = stack.get()
                    accum += (last_valid+before_last)
                    stack.put(before_last)
                    stack.put(last_valid)
                    stack.put(before_last + last_valid)
        return accum
        