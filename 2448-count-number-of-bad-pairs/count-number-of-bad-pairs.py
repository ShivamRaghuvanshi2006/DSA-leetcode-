class Solution:
    def countBadPairs(self, nums):
        from collections import Counter
        c=Counter()
        good=0
        for i,x in enumerate(nums):
            k=x-i
            good+=c[k]
            c[k]+=1
        n=len(nums)
        return n*(n-1)//2-good
