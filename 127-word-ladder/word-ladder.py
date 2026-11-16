class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import deque
        s=set(wordList)
        if endWord not in s: return 0
        q=deque([(beginWord,1)])
        vis={beginWord}
        while q:
            w,d=q.popleft()
            if w==endWord: return d
            for i in range(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nw=w[:i]+c+w[i+1:]
                    if nw in s and nw not in vis:
                        vis.add(nw); q.append((nw,d+1))
        return 0