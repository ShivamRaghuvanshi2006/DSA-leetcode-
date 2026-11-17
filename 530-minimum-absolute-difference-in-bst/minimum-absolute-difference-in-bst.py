class Solution:
    def getMinimumDifference(self, root):
        self.prev = None; self.best = 10**9
        def dfs(n):
            if not n: return
            dfs(n.left)
            if self.prev is not None:
                self.best = min(self.best, abs(n.val - self.prev))
            self.prev = n.val
            dfs(n.right)
        dfs(root)
        return self.best
