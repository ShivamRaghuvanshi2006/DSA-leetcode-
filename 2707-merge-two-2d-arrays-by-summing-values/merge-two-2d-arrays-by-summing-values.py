class Solution:
    def mergeArrays(self, a, b):
        from collections import defaultdict
        d=defaultdict(int)
        for k,v in a+b:
            d[k]+=v
        return sorted(d.items())
