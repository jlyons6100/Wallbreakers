class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ind = 0
        while ind < len(intervals)-1:
            if intervals[ind][0] <= intervals[ind+1][0] and intervals[ind][1] >= intervals[ind+1][0]:
                minn = min(intervals[ind][0], intervals[ind+1][0])
                maxx = max(intervals[ind+1][1], intervals[ind][1])
                del intervals[ind]
                intervals[ind] = [minn, maxx]
            else:
                ind += 1
        return(intervals)