class Solution:
    def lastRemaining(self, n: int) -> int:
        head=1
        step=1
        rem=n
        left=True
        while rem>1:
            if left or rem%2==1:
                head+=step
            rem//=2
            step*=2
            left=not left
        return head