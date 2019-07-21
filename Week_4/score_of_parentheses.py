from queue import LifoQueue as Stack
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # stack = Stack()
        # for ltr in S:
        #     if ltr == '(':
        #         stack.put(0)
        #     else:
        #         val = stack.get()
        #         if stack.qsize() > 0:
        #             if val == 0:
        #                 prev = stack.get()
        #                 prev += 1
        #                 stack.put(prev)
        #             else:
        #                 prev = stack.get()
        #                 prev += val*2
        #                 stack.put(prev)
        #         else:
        #             if val == 0:
        #                 stack.put(1)
        #             else:
        #                 stack.put(val*2)
        # return stack.get()
        cur_level = 0
        stack = Stack()
        for ltr in S:
            if ltr == '(':
                stack.put(cur_level)
                cur_level = 0
            else:
                maxx = max(1, cur_level)
                cur_level += stack.get() + maxx
                
        return(cur_level)