class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        s = 0
        if root.left and not root.left.left and not root.left.right:
            s += root.left.val
        return s + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
