# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root) -> int:
        self.prev=None; self.best=10**9
        def dfs(n):
            if not n: return
            dfs(n.left)
            if self.prev is not None: self.best=min(self.best,n.val-self.prev)
            self.prev=n.val
            dfs(n.right)
        dfs(root)
        return self.best