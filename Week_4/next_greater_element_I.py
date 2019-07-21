from queue import PriorityQueue
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pQ = PriorityQueue()
        mapping = {}
        for num in nums2:
            if not pQ.empty():
                little = pQ.get()
                while(little < num):
                    mapping[little] = num
                    if pQ.empty():
                        break
                    little = pQ.get()
                if little >= num:
                    pQ.put(little)
                pQ.put(num)
            else:
                pQ.put(num)
        return [mapping[key] if key in mapping else -1 for key in nums1 ]
        