class Solution:
    def numIslands(self, grid):
        R,C=len(grid),len(grid[0]); cnt=0
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or grid[r][c]!='1': return
            grid[r][c]='0'
            dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1)
        for i in range(R):
            for j in range(C):
                if grid[i][j]=='1': cnt+=1; dfs(i,j)
        return cnt