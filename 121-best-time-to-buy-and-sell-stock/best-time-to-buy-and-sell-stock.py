class Solution:
    def maxProfit(self, prices):
        mn = float('inf')
        best = 0
        for p in prices:
            mn = min(mn, p)
            best = max(best, p - mn)
        return best
