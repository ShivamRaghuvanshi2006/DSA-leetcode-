class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        r=[]
        for x in range(left,right+1):
            s=str(x)
            if '0' in s: continue
            if all(x%int(d)==0 for d in s): r.append(x)
        return r