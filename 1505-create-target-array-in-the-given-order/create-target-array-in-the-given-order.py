class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        r=[]
        for v,i in zip(nums,index): r.insert(i,v)
        return r