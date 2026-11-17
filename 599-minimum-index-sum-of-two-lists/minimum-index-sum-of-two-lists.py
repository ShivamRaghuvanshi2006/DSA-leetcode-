class Solution:
    def findRestaurant(self, a, b):
        pos = {x: i for i, x in enumerate(a)}
        best = 10**9; res = []
        for j, x in enumerate(b):
            if x in pos:
                s = pos[x] + j
                if s < best:
                    best = s; res = [x]
                elif s == best:
                    res.append(x)
        return res
