class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        cnt = 0
        for i, x in enumerate(nums):
            if i == 0:
                if x >= nums[1]:
                    cnt += 1
            elif i == n - 1:
                if x >= nums[n-2]:
                    cnt += 1
            else:
                if x * 2 >= nums[i-1] + nums[i+1]:
                    cnt += 1
        return cnt