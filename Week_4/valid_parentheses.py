import queue
class Solution:
    def isValid(self, s: str) -> bool:
        q = queue.LifoQueue()
        for ltr in s:
            if ltr == '(' or ltr == '{' or ltr == '[':
                q.put(ltr)
            else:
                if q.empty():
                    return False
                else:
                    brack = q.get()
                    if brack == '(':
                        if ltr != ')':
                            return False
                    elif brack == '{':
                        if ltr != '}':
                            return False
                    elif brack == '[':
                        if ltr != ']':
                            return False   
        return q.empty()