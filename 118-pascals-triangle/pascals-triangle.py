class Solution:
    def generate(self, numRows):
        res=[[1]]
        for i in range(1,numRows):
            prev=res[-1]
            row=[1]+[prev[j]+prev[j+1] for j in range(len(prev)-1)]+[1]
            res.append(row)
        return res