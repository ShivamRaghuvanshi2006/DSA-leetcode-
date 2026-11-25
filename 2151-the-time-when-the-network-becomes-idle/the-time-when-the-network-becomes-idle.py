class Solution:
    def networkBecomesIdle(self, edges, patience):
        from collections import deque
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        dist = [-1]*n
        dist[0]=0
        q=deque([0])
        while q:
            u=q.popleft()
            for w in g[u]:
                if dist[w]==-1:
                    dist[w]=dist[u]+1
                    q.append(w)
        ans=0
        for i in range(1,n):
            r=dist[i]*2
            p=patience[i]
            if r<=p:
                last=r
            else:
                last=((r-1)//p)*p+r
            ans=max(ans,last)
        return ans+1
