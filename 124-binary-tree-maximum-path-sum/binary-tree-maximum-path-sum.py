class Solution:
    def maxPathSum(self, root):
        self.ans=float('-inf')
        def dfs(n):
            if not n: return 0
            l=max(0,dfs(n.left)); r=max(0,dfs(n.right))
            self.ans=max(self.ans,n.val+l+r)
            return n.val+max(l,r)
        dfs(root)
        return self.ans