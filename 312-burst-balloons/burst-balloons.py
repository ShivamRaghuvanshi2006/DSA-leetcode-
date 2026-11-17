class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        a=[1]+nums+[1]; n=len(a)
        dp=[[0]*n for _ in range(n)]
        for l in range(2,n):
            for i in range(n-l):
                j=i+l
                best=0
                for k in range(i+1,j):
                    v=a[i]*a[k]*a[j]+dp[i][k]+dp[k][j]
                    if v>best: best=v
                dp[i][j]=best
        return dp[0][n-1]
