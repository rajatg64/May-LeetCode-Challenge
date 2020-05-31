from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points
        res = []
        for x,y in points:
            dis = math.sqrt(x**2 + y**2)
            if len(res) == K:
                heappushpop(res,[-dis,x,y])
            else:
                heappush(res,[-dis,x,y])
        return [[x,y] for _,x,y in res]