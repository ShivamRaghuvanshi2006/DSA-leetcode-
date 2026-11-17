class Solution:
    def findLHS(self, nums):
        from collections import Counter
        c = Counter(nums)
        return max([c[x] + c.get(x+1, 0) for x in c if x+1 in c] or [0])
