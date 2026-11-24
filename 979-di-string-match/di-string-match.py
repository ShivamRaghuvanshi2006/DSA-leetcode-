class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        lo,hi=0,len(s); r=[]
        for ch in s:
            if ch=='I': r.append(lo); lo+=1
            else: r.append(hi); hi-=1
        r.append(lo)
        return r