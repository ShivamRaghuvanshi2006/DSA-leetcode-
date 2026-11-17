class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def ispal(s,l,r):
            while l<r:
                if s[l]!=s[r]: return False
                l+=1; r-=1
            return True
        mp={w:i for i,w in enumerate(words)}
        res=set()
        for i,w in enumerate(words):
            n=len(w)
            for j in range(n+1):
                # w[j:] palindrome -> need reversed w[:j]
                if ispal(w,j,n-1):
                    need=w[:j][::-1]
                    if need in mp and mp[need]!=i:
                        res.add((i,mp[need]))
                if j>0 and ispal(w,0,j-1):
                    need=w[j:][::-1]
                    if need in mp and mp[need]!=i:
                        res.add((mp[need],i))
        return [list(x) for x in res]
