class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n=len(arr); res=[]
        for x in arr:
            res.append(x)
            if x==0: res.append(0)
            if len(res)>=n: break
        for i in range(n): arr[i]=res[i]