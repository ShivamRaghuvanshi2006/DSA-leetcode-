class Solution:
    def findMaxConsecutiveOnes(self, nums):
        b = c = 0
        for x in nums:
            c = c + 1 if x == 1 else 0
            b = max(b, c)
        return b
