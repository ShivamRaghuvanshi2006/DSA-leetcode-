class Solution:
    def numberOfPoints(self, nums):
        s=set()
        for a,b in nums:
            for x in range(a,b+1):
                s.add(x)
        return len(s)
