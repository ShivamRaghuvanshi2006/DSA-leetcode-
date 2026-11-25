class Solution:
    def countKDifference(self, nums, k):
        from collections import Counter
        c=Counter(nums)
        ans=0
        for x in c:
            if x+k in c:
                ans+=c[x]*c[x+k]
        return ans
