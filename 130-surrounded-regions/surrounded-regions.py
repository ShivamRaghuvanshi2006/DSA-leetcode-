class Solution:
    def solve(self, board):
        if not board: return
        R,C=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or board[r][c]!='O': return
            board[r][c]='S'
            dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1)
        import sys; sys.setrecursionlimit(100000)
        for i in range(R): dfs(i,0); dfs(i,C-1)
        for j in range(C): dfs(0,j); dfs(R-1,j)
        for i in range(R):
            for j in range(C):
                board[i][j]='O' if board[i][j]=='S' else 'X'