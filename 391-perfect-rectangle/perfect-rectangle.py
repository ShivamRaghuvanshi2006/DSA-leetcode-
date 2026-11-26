class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        area=0
        corners=set()
        minx=miny=10**9
        maxa=maxb=-10**9
        for x,y,a,b in rectangles:
            area+=(a-x)*(b-y)
            minx=min(minx,x); miny=min(miny,y)
            maxa=max(maxa,a); maxb=max(maxb,b)
            for p in [(x,y),(x,b),(a,y),(a,b)]:
                if p in corners: corners.remove(p)
                else: corners.add(p)
        if len(corners)!=4: return False
        if (minx,miny) not in corners: return False
        if (minx,maxb) not in corners: return False
        if (maxa,miny) not in corners: return False
        if (maxa,maxb) not in corners: return False
        return area==(maxa-minx)*(maxb-miny)