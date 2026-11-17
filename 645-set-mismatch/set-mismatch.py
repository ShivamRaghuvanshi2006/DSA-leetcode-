class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        s = set(nums)
        dup = sum(nums) - sum(s)
        miss = n*(n+1)//2 - sum(s)
        return [dup, miss]
