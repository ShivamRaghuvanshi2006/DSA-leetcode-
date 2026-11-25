class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        h=[-x for x in stones]; heapq.heapify(h)
        while len(h)>1:
            a=-heapq.heappop(h); b=-heapq.heappop(h)
            if a!=b: heapq.heappush(h,-(a-b))
        return -h[0] if h else 0