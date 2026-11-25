class Solution:
    def countFairPairs(self, nums, lower, upper):
        import bisect
        nums.sort()
        ans=0
        for i,x in enumerate(nums):
            l=bisect.bisect_left(nums,lower-x,i+1)
            r=bisect.bisect_right(nums,upper-x,i+1)
            # need j>i so count in (i+1..)
            import bisect as b
            l=b.bisect_left(nums,lower-x,i+1)
            r=b.bisect_right(nums,upper-x,i+1)
            ans+=max(0,r-max(l,i+1))
        return ans
