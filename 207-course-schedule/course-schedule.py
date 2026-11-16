class Solution:
    def canFinish(self, n, pre):
        from collections import defaultdict,deque
        g=defaultdict(list); ind=[0]*n
        for a,b in pre: g[b].append(a); ind[a]+=1
        q=deque([i for i in range(n) if ind[i]==0]); v=0
        while q:
            u=q.popleft(); v+=1
            for w in g[u]:
                ind[w]-=1
                if ind[w]==0: q.append(w)
        return v==n