class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        from collections import Counter
        need=Counter(c.lower() for c in licensePlate if c.isalpha())
        best=None
        for w in words:
            c=Counter(w)
            if all(c[k]>=v for k,v in need.items()):
                if best is None or len(w)<len(best): best=w
        return best