class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        slow,fast=head,head.next
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        mid=slow.next; slow.next=None
        l=self.sortList(head); r=self.sortList(mid)
        d=ListNode(0); c=d
        while l and r:
            if l.val<r.val: c.next=l; l=l.next
            else: c.next=r; r=r.next
            c=c.next
        c.next=l or r
        return d.next