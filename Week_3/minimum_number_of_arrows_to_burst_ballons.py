class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []:
            return 0
        points.sort(reverse = True)
        cur = points[0][0]
        accum = 1
        for point in points:
            if cur > point[1]:
                accum += 1
                cur = point[0]
        return accum