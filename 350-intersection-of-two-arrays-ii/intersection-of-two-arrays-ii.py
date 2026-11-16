class Solution:
    def intersect(self, a, b):
        from collections import Counter
        c, d = Counter(a), Counter(b)
        res = []
        for k in c:
            if k in d:
                res += [k] * min(c[k], d[k])
        return res
