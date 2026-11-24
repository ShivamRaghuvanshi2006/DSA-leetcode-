class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n=len(arr)
        if n<3 or arr[0]>=arr[1]: return False
        i=1
        while i+1<n and arr[i]<arr[i+1]: i+=1
        if i==n-1: return False
        while i+1<n:
            if arr[i]<=arr[i+1]: return False
            i+=1
        return True