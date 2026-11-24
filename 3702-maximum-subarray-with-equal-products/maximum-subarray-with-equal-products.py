from typing import List
from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        def prime_mask(x: int) -> int:
            m = 0
            if x % 2 == 0:
                m |= 1
            if x % 3 == 0:
                m |= 2
            if x % 5 == 0:
                m |= 4
            if x % 7 == 0:
                m |= 8
            return m
        best = 2
        for l in range(n):
            used = 0
            for r in range(l, n):
                m = prime_mask(nums[r])
                if used & m:
                    break
                used |= m
                cur = r - l + 1
                if cur > best:
                    best = cur
                    if best == n:
                        return best
        return best
