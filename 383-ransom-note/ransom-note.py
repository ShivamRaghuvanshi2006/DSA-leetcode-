class Solution:
    def canConstruct(self, r, m):
        from collections import Counter
        c, d = Counter(r), Counter(m)
        return all(c[k] <= d.get(k, 0) for k in c)
