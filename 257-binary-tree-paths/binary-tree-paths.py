class Solution:
    def binaryTreePaths(self, root):
        res = []
        def dfs(n, p):
            if not n:
                return
            p += str(n.val)
            if not n.left and not n.right:
                res.append(p)
            else:
                dfs(n.left, p + '->'); dfs(n.right, p + '->')
        dfs(root, '')
        return res
