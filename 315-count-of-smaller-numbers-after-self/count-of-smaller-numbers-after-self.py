class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        s=sorted(set(nums)); mp={v:i+1 for i,v in enumerate(s)}
        bit=[0]*(len(s)+2)
        def add(i):
            while i<len(bit):
                bit[i]+=1; i+=i&-i
        def q(i):
            r=0
            while i:
                r+=bit[i]; i-=i&-i
            return r
        ans=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            ans[i]=q(mp[nums[i]]-1); add(mp[nums[i]])
        return ans
