class Solution:
    def findTarget(self, root, k):
        seen = set()
        st = [root]
        while st:
            n = st.pop()
            if not n: continue
            if k - n.val in seen: return True
            seen.add(n.val)
            st += [n.left, n.right]
        return False
