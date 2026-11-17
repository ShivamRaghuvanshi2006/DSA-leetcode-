class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        ws=set(wordDict); n=len(s)
        can=[False]*(n+1); can[n]=True
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                if s[i:j] in ws and can[j]:
                    can[i]=True; break
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i):
            if i==n: return [""]
            out=[]
            for j in range(i+1,n+1):
                w=s[i:j]
                if w in ws and can[j]:
                    for rest in dfs(j):
                        out.append(w if not rest else w+" "+rest)
            return out
        return dfs(0) if can[0] else []
