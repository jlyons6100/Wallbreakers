class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        beg = 0
        end = len(A) - 1
        mid = int((beg + end) / 2)
        while(beg <= end):
            if A[mid-1] < A[mid] and A[mid + 1] < A[mid]:
                return mid
            elif A[mid-1] >= A[mid]:
                end = mid - 1
                mid = int((beg + end) / 2)   
            elif A[mid] <= A[mid + 1]:
                beg = mid + 1
                mid = int((beg + end) / 2)
        if A[mid-1] < A[mid] and A[mid + 1] > A[mid]:
            return mid
        else:
            return -1