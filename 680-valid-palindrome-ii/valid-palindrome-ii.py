class Solution:
    def validPalindrome(self, s):
        def ok(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1; r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return ok(l+1, r) or ok(l, r-1)
            l += 1; r -= 1
        return True
