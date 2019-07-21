from queue import PriorityQueue as PQ
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PQ()
        head_prev = ListNode(0)
        cur = head_prev
        for i_list in lists:
            while(i_list != None):
                pq.put(i_list.val)
                i_list = i_list.next
        while (not pq.empty()):
            cur.next = ListNode(pq.get())
            cur = cur.next
        return head_prev.next
        # First Solution: comparing nodes and increasing pointer of lists that aren't empty
        # curs = lists
        # head_prev = ListNode(0)
        # cur = head_prev
        # while (curs != []):
        #     smallest = sys.maxsize
        #     node = None
        #     my_i = 0
        #     for i in range(len(curs)):
        #         i_node = curs[i]
        #         if i_node.val < smallest:
        #             smallest = i_node.val
        #             node = i_node
        #             my_i = i
        #     cur.next = ListNode(smallest)
        #     cur = cur.next
        #     if node.next == None:
        #         del curs[my_i]
        #     else:
        #         curs[my_i] = curs[my_i].next
        # return head_prev.next