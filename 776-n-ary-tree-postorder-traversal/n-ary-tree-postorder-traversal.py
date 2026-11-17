class Solution:
    def postorder(self, root):
        res = []
        def dfs(n):
            if not n: return
            for ch in n.children:
                dfs(ch)
            res.append(n.val)
        dfs(root)
        return res
