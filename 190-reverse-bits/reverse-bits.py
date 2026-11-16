class Solution:
    def reverseBits(self, n):
        r = 0
        for _ in range(32):
            r = (r << 1) | (n & 1)
            n >>= 1
        return r
