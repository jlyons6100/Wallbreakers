# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        prev = None
        cur = head
        n = head.next
        
        while(cur != None):
            cur.next = prev
            prev = cur
            cur = n
            if n != None:
                n = n.next
            
        return prev