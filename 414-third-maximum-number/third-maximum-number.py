class Solution:
    def thirdMax(self, nums):
        s = sorted(set(nums), reverse=True)
        return s[2] if len(s) >= 3 else s[0]
