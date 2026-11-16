class Solution:
    def connect(self, root):
        cur=root
        while cur:
            dummy=TreeNode(0); tail=dummy; n=cur; cur=None
            while n:
                if n.left:
                    tail.next=n.left; tail=tail.next
                    if not cur: cur=n.left
                if n.right:
                    tail.next=n.right; tail=tail.next
                    if not cur: cur=n.right
                n=n.next
        return root