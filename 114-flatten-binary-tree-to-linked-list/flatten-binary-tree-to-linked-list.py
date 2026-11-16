class Solution:
    def flatten(self, root):
        cur=root
        while cur:
            if cur.left:
                p=cur.left
                while p.right: p=p.right
                p.right=cur.right
                cur.right=cur.left
                cur.left=None
            cur=cur.right