class Solution:
    def arrangeCoins(self, n):
        import math
        return int((math.sqrt(1 + 8 * n) - 1) // 2)
