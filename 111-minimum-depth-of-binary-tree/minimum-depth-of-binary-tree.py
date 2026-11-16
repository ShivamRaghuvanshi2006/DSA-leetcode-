class Solution:
    def minDepth(self, root):
        if not root: return 0
        from collections import deque
        q=deque([(root,1)])
        while q:
            n,d=q.popleft()
            if not n.left and not n.right: return d
            if n.left: q.append((n.left,d+1))
            if n.right: q.append((n.right,d+1))