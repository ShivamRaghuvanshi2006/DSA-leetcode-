class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie={}
        for w in words:
            t=trie
            for c in w:
                t=t.setdefault(c,{})
            t['#']=w
        m,n=len(board),len(board[0]); res=set()
        import sys; sys.setrecursionlimit(1000000)
        def dfs(i,j,t):
            c=board[i][j]
            if c not in t: return
            nt=t[c]
            if '#' in nt: res.add(nt['#'])
            board[i][j]='.'
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and board[ni][nj]!='.':
                    dfs(ni,nj,nt)
            board[i][j]=c
        for i in range(m):
            for j in range(n):
                dfs(i,j,trie)
        return list(res)
