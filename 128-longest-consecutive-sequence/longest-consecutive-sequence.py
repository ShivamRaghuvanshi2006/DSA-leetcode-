class Solution:
    def longestConsecutive(self, nums):
        s=set(nums); best=0
        for x in s:
            if x-1 not in s:
                c=1; y=x
                while y+1 in s: y+=1; c+=1
                best=max(best,c)
        return best