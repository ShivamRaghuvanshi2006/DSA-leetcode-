class Solution:
    def findTheDifference(self, s, t):
        r = 0
        for c in s + t:
            r ^= ord(c)
        return chr(r)
