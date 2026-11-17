class Solution:
    def nextGreaterElement(self, a, b):
        pos = {x: i for i, x in enumerate(b)}
        res = []
        for x in a:
            f = -1
            for y in b[pos[x]+1:]:
                if y > x:
                    f = y; break
            res.append(f)
        return res
