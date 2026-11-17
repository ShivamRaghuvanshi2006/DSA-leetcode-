class Solution:
    def diameterOfBinaryTree(self, root):
        self.b = 0
        def d(n):
            if not n: return 0
            l, r = d(n.left), d(n.right)
            self.b = max(self.b, l + r)
            return 1 + max(l, r)
        d(root)
        return self.b
