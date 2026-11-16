class Solution:
    def preorderTraversal(self, root):
        res, st = [], [root]
        while st:
            n = st.pop()
            if n:
                res.append(n.val)
                st.append(n.right); st.append(n.left)
        return res
