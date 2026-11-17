import heapq
class Solution:
    def mergeKLists(self, lists):
        pq=[]
        for i,h in enumerate(lists):
            if h: heapq.heappush(pq,(h.val,i,h))
        dummy=None
        if lists:
            # find node class
            for h in lists:
                if h:
                    dummy=h.__class__(0); break
            if dummy is None: return None
        else: return None
        cur=dummy
        while pq:
            _,i,n=heapq.heappop(pq)
            cur.next=n; cur=cur.next
            if n.next: heapq.heappush(pq,(n.next.val,i,n.next))
        return dummy.next
