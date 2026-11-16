class Solution:
    def postorderTraversal(self, root):
        res, st = [], [root]
        while st:
            n = st.pop()
            if n:
                res.append(n.val)
                st.append(n.left); st.append(n.right)
        return res[::-1]
