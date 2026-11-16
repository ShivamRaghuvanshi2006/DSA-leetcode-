class Solution:
    def isPerfectSquare(self, n):
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if m * m == n:
                return True
            if m * m < n:
                l = m + 1
            else:
                r = m - 1
        return False
