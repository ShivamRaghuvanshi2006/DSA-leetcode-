class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        mx=-1
        for i in range(len(arr)-1,-1,-1):
            arr[i],mx=mx,max(mx,arr[i])
        return arr