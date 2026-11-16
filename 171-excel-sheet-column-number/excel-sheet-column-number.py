class Solution:
    def titleToNumber(self, s):
        r = 0
        for c in s:
            r = r * 26 + ord(c) - 64
        return r
