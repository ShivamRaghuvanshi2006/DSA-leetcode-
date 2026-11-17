class Solution:
    def averageOfLevels(self, root):
        from collections import deque
        q = deque([root])
        res = []
        while q:
            s = 0; n = len(q)
            for _ in range(n):
                nd = q.popleft()
                s += nd.val
                if nd.left: q.append(nd.left)
                if nd.right: q.append(nd.right)
            res.append(s / n)
        return res
