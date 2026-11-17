class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n=len(s); INF=10**9
        cost=[[INF]*n for _ in range(n)]
        for l in range(n):
            for r in range(l+1,n):
                L=r-l+1; t=s[l:r+1]; best=INF
                for d in range(1,L):
                    if L%d!=0: continue
                    cur=0
                    for g in range(d):
                        seq=[t[idx] for idx in range(g,L,d)]
                        i,j=0,len(seq)-1
                        while i<j:
                            if seq[i]!=seq[j]: cur+=1
                            i+=1; j-=1
                    if cur<best: best=cur
                cost[l][r]=best
        dp=[[INF]*(k+1) for _ in range(n+1)]
        dp[n][0]=0
        for i in range(n-1,-1,-1):
            for p in range(1,k+1):
                for j in range(i+1,n):
                    if cost[i][j]>=INF: continue
                    if dp[j+1][p-1]>=INF: continue
                    v=cost[i][j]+dp[j+1][p-1]
                    if v<dp[i][p]: dp[i][p]=v
        return dp[0][k]
