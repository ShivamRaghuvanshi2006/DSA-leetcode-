from math import gcd
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        if n<=2: return n
        ans=1
        for i in range(n):
            mp={}; dup=0; best=0
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dx,dy=x2-x1,y2-y1
                if dx==0 and dy==0:
                    dup+=1; continue
                g=gcd(dx,dy); dx//=g; dy//=g
                if dx<0 or (dx==0 and dy<0): dx,dy=-dx,-dy
                mp[(dx,dy)]=mp.get((dx,dy),0)+1
                best=max(best,mp[(dx,dy)])
            ans=max(ans,best+dup+1)
        return ans
