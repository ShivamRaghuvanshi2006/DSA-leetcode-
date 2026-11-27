class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            cur_and = nums[l]
            cur_min = nums[l]
            for r in range(l, n):
                if r > l:
                    cur_and &= nums[r]
                    if nums[r] < cur_min:
                        cur_min = nums[r]
                if cur_and == cur_min:
                    ans += 1
        return ans