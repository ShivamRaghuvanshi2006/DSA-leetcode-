class Solution:
    def convertToBase7(self, n):
        if n == 0:
            return '0'
        neg = n < 0
        n = abs(n)
        r = ''
        while n:
            r = str(n % 7) + r
            n //= 7
        return ('-' if neg else '') + r
