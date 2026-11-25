"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = [root]
        while q:
            res.append([n.val for n in q])
            nxt = []
            for n in q:
                if n.children:
                    nxt.extend(n.children)
            q = nxt
        return res
