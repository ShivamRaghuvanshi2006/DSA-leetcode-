class Solution:
    def minimumPushes(self, word):
        from collections import Counter
        f=sorted(Counter(word).values(),reverse=True)
        return sum(v*((i//8)+1) for i,v in enumerate(f))
