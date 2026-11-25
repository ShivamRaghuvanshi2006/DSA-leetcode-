class Solution:
    def romanToInt(self, s):
        m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        prev=0
        for ch in reversed(s):
            v=m[ch]
            if v<prev:
                ans-=v
            else:
                ans+=v
            prev=max(prev,v)
        return ans
