class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n==1 and not trust: return 1
        cnt=[0]*(n+1); out=[0]*(n+1)
        for a,b in trust:
            out[a]+=1; cnt[b]+=1
        for i in range(1,n+1):
            if cnt[i]==n-1 and out[i]==0: return i
        return -1