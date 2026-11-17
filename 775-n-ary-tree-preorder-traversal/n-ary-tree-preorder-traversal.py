class Solution:
    def preorder(self, root):
        res = []
        def dfs(n):
            if not n: return
            res.append(n.val)
            for ch in n.children:
                dfs(ch)
        dfs(root)
        return res
