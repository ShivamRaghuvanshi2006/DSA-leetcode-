class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res=[]; n=len(num)
        def dfs(i,path,val,last):
            if i==n:
                if val==target: res.append(path)
                return
            for j in range(i,n):
                if j>i and num[i]=='0': break
                cur=int(num[i:j+1])
                if i==0:
                    dfs(j+1,num[i:j+1],cur,cur)
                else:
                    dfs(j+1,path+'+'+num[i:j+1],val+cur,cur)
                    dfs(j+1,path+'-'+num[i:j+1],val-cur,-cur)
                    dfs(j+1,path+'*'+num[i:j+1],val-last+last*cur,last*cur)
        dfs(0,"",0,0)
        return res
