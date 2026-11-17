class Solution:
    def tree2str(self, t):
        if not t: return ''
        l = '(' + self.tree2str(t.left) + ')' if (t.left or t.right) else ''
        r = '(' + self.tree2str(t.right) + ')' if t.right else ''
        return str(t.val) + l + r
