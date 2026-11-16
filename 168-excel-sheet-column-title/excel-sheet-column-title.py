class Solution:
    def convertToTitle(self, n):
        res = ''
        while n:
            n -= 1
            res = chr(n % 26 + 65) + res
            n //= 26
        return res
