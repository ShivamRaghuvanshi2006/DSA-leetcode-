# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root):
        from collections import defaultdict
        freq = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            freq[s] += 1
            return s
        dfs(root)
        mx = max(freq.values())
        return [k for k, v in freq.items() if v == mx]
