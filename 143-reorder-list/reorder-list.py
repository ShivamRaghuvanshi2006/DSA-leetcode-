class Solution:
    def reorderList(self, head):
        if not head: return
        slow=fast=head
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        prev=None; cur=slow.next; slow.next=None
        while cur:
            nxt=cur.next; cur.next=prev; prev=cur; cur=nxt
        a=head; b=prev
        while b:
            an=a.next; bn=b.next; a.next=b; b.next=an; a=an; b=bn