class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n=len(prices)
        if n<=1 or k==0: return 0
        if k>=n//2:
            return sum(max(0,prices[i+1]-prices[i]) for i in range(n-1))
        buy=[-10**9]*k; sell=[0]*k
        for p in prices:
            for i in range(k):
                ps=sell[i-1] if i>0 else 0
                if ps-p>buy[i]: buy[i]=ps-p
                if buy[i]+p>sell[i]: sell[i]=buy[i]+p
        return sell[-1]
