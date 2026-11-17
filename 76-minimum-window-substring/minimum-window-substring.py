from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t); missing=len(t); l=0; bi,bj=0,10**9
        for r,c in enumerate(s):
            if need[c]>0: missing-=1
            need[c]-=1
            while missing==0:
                if r-l<bj-bi: bi,bj=l,r
                need[s[l]]+=1
                if need[s[l]]>0: missing+=1
                l+=1
        return "" if bj==10**9 else s[bi:bj+1]
