# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ret = head
        if ret == None:
            return ret
        elif ret.next == None:
            return ret
        cur = head
        pre_odd = ListNode(0)
        pre_even = ListNode(0)
        saved_o = pre_odd
        saved_e = pre_even
        while(cur != None):
            pre_odd.next = ListNode(cur.val)
            if cur.next == None:
                break
            pre_even.next = ListNode(cur.next.val)
            pre_odd = pre_odd.next
            pre_even = pre_even.next
            cur = cur.next.next
        if pre_odd.next != None:
            pre_odd.next.next = saved_e.next
        else:
            pre_odd.next = saved_e.next
        return saved_o.next