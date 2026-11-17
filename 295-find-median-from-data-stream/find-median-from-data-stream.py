import heapq
class MedianFinder:
    def __init__(self):
        self.a=[]; self.b=[]
    def addNum(self, x: int) -> None:
        heapq.heappush(self.a,-x)
        heapq.heappush(self.b,-heapq.heappop(self.a))
        if len(self.b)>len(self.a):
            heapq.heappush(self.a,-heapq.heappop(self.b))
    def findMedian(self) -> float:
        if len(self.a)>len(self.b): return -self.a[0]
        return (-self.a[0]+self.b[0])/2
