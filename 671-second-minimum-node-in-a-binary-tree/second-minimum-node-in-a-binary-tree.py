class Solution:
    def findSecondMinimumValue(self, root):
        vals = set()
        def dfs(n):
            if not n: return
            vals.add(n.val); dfs(n.left); dfs(n.right)
        dfs(root)
        s = sorted(vals)
        return s[1] if len(s) > 1 else -1
