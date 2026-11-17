class Solution:
    def canPlaceFlowers(self, f, n):
        f = [0] + f + [0]
        for i in range(1, len(f) - 1):
            if f[i-1] == f[i] == f[i+1] == 0:
                f[i] = 1; n -= 1
        return n <= 0
