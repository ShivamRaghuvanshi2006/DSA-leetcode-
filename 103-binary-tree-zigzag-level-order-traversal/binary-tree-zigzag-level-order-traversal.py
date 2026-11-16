class Solution:
    def zigzagLevelOrder(self, root):
        from collections import deque
        if not root: return []
        q=deque([root]); res=[]; left=True
        while q:
            level=[]
            for _ in range(len(q)):
                n=q.popleft()
                level.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            if not left: level=level[::-1]
            res.append(level)
            left=not left
        return res