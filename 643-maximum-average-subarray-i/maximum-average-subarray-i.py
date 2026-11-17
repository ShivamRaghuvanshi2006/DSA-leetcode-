class Solution:
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k]); b = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            b = max(b, s)
        return b / k
