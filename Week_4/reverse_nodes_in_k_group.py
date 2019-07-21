# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def count_remaining(self, cur):
        accum = 0
        while(cur != None):
            cur = cur.next
            accum += 1
        return accum
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k > self.count_remaining(head) or k == 1:
            return head
        ret = None
        prev = None
        cur = head
        now_last = head
        nextt = head.next
        remainder = None
        for x in range(k):
            cur.next = prev
            prev = cur
            ret = prev
            cur = nextt
            if cur == None:
                return ret
            if cur.next == None:
                remainder = nextt
            nextt = cur.next
        while(self.count_remaining(cur) >= k):
            prev = None
            temp_last = cur
            entered_loop = True
            for x in range(k):
                cur.next = prev
                prev = cur
                cur = nextt
                if cur == None:
                    break
                if cur.next == None:
                    remainder = nextt
                nextt = cur.next
            now_last.next = prev
            now_last = temp_last
        if self.count_remaining(cur) == 0:
            pass
        elif remainder != None:
            now_last.next = remainder
        else:
            now_last.next = cur
        return ret