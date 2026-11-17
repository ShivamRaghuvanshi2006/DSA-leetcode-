from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q=deque(); out=[]
        for i,v in enumerate(nums):
            while q and nums[q[-1]]<=v: q.pop()
            q.append(i)
            if q[0]<=i-k: q.popleft()
            if i>=k-1: out.append(nums[q[0]])
        return out
