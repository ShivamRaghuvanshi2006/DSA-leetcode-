class Solution:
    def findRelativeRanks(self, s):
        order = sorted(range(len(s)), key=lambda i: -s[i])
        r = [''] * len(s)
        for rank, i in enumerate(order):
            if rank == 0: r[i] = 'Gold Medal'
            elif rank == 1: r[i] = 'Silver Medal'
            elif rank == 2: r[i] = 'Bronze Medal'
            else: r[i] = str(rank + 1)
        return r
