class Solution:
    def sumNumbers(self, root):
        self.ans=0
        def dfs(n,v):
            if not n: return
            v=v*10+n.val
            if not n.left and not n.right: self.ans+=v
            else: dfs(n.left,v); dfs(n.right,v)
        dfs(root,0)
        return self.ans