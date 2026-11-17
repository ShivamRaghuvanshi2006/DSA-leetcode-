class Solution:
    def findLengthOfLCIS(self, nums):
        b = c = 1
        for i in range(1, len(nums)):
            c = c + 1 if nums[i] > nums[i-1] else 1
            b = max(b, c)
        return b
