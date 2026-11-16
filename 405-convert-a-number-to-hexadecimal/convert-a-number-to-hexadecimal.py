class Solution:
    def toHex(self, num):
        if num == 0:
            return '0'
        num &= 0xffffffff
        h = '0123456789abcdef'
        r = ''
        while num:
            r = h[num % 16] + r
            num //= 16
        return r
