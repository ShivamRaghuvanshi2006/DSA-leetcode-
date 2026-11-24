class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        d={c:i for i,c in enumerate(order)}
        def key(w): return [d[c] for c in w]
        return all(key(words[i])<=key(words[i+1]) for i in range(len(words)-1))