class Solution:
    def connect(self, root):
        if not root: return root
        l=root
        while l.left:
            h=l
            while h:
                h.left.next=h.right
                if h.next: h.right.next=h.next.left
                h=h.next
            l=l.left
        return root