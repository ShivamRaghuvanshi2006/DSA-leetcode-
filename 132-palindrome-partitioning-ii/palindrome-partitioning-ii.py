class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPal = [[False]*n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                isPal[i][j] = (s[i]==s[j]) and (l<=3 or isPal[i+1][j-1])
        dp = [0]*n
        for i in range(n):
            if isPal[0][i]:
                dp[i]=0
            else:
                best=n
                for k in range(i):
                    if isPal[k+1][i]:
                        if dp[k]+1<best: best=dp[k]+1
                dp[i]=best
        return dp[n-1]
