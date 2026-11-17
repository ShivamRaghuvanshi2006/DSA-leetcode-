import heapq
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        ev=[]
        for l,r,h in buildings:
            ev.append((l,-h,r)); ev.append((r,0,0))
        ev.sort()
        res=[]; heap=[(0,float('inf'))]
        for x,nh,r in ev:
            while heap[0][1]<=x: heapq.heappop(heap)
            if nh: heapq.heappush(heap,(nh,r))
            h=-heap[0][0]
            if not res or res[-1][1]!=h:
                res.append([x,h])
        return res
