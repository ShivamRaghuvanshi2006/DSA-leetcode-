# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        def h(n):
            if not n:
                return 0
            l = h(n.left)
            if l == -1:
                return -1
            r = h(n.right)
            if r == -1 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)
        return h(root) != -1
