class Solution:
    def interchangeableRectangles(self, rectangles):
        from collections import Counter
        from math import gcd
        c=Counter()
        for w,h in rectangles:
            g=gcd(w,h)
            c[(w//g,h//g)]+=1
        return sum(v*(v-1)//2 for v in c.values())
