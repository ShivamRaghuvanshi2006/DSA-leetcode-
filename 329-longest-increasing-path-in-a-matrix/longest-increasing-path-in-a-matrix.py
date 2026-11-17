class Solution:
    def longestIncreasingPath(self, mat: list[list[int]]) -> int:
        m,n=len(mat),len(mat[0])
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i,j):
            b=1
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and mat[ni][nj]>mat[i][j]:
                    v=1+dfs(ni,nj)
                    if v>b: b=v
            return b
        return max(dfs(i,j) for i in range(m) for j in range(n))
