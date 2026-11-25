# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        from collections import deque
        q=deque([(root,None,0)])
        ax=ay=None
        while q:
            n,p,d=q.popleft()
            if n.val==x: ax=(p,d)
            if n.val==y: ay=(p,d)
            if n.left: q.append((n.left,n,d+1))
            if n.right: q.append((n.right,n,d+1))
        return ax is not None and ay is not None and ax[0]!=ay[0] and ax[1]==ay[1]