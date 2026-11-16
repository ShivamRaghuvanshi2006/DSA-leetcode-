class Solution:
    def reverseList(self, head):
        p=None
        while head: head.next,head,p=p,head.next,head
        return p