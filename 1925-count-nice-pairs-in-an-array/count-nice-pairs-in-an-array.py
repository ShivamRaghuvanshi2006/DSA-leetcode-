class Solution:
    def countNicePairs(self, nums):
        from collections import Counter
        MOD=10**9+7
        def rev(x):
            return int(str(x)[::-1])
        c=Counter(x-rev(x) for x in nums)
        return sum(v*(v-1)//2 for v in c.values())%MOD
