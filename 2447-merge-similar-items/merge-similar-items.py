class Solution:
    def mergeSimilarItems(self, a, b):
        from collections import Counter
        c=Counter()
        for k,v in a+b:
            c[k]+=v
        return sorted(c.items())
